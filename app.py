from flask import Flask, render_template, request, redirect
from markupsafe import escape
import os
import csv
from data import DB
from datetime import datetime
from flask.helpers import url_for
import calendar

# web application instance
app = Flask(__name__)


#database setup using sqlalchemy --change the database name accordingly
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#db = SQLAlchemy(app)

#-------------------------Alchemy Models--------------------------------------- 

#-------------------------lists and veriables--------------------------------------- 


#-------------------------routing--------------------------------------- 

@app.route("/", methods=["GET", "POST"])
def index():
    page = "Dashboard"
    today = 'Monday June 34, 2021'
    runningJobs = DB.RunningJobsCount()
    dayCount = DB.getJobsCompleteToday()
    weekCount = DB.getJobsCompleteThisWeek()
    monthCount = DB.getJobsCompleteThisMonth()

    output = {
        'runningJobs' : runningJobs,
        'dayCount' : dayCount,
        'weekCount' : weekCount,
        'monthCount' : monthCount
    }

    return render_template('index.html', output=output, page=page, today=today)





@app.route("/update_job/<jobID>")
def updateJob(jobID):
    page = "Update job"
    oplist = DB.getActiveOperators()
    typeList = DB.getJobType()
    workcellList = DB.getWorkCells()
    result = DB.setUpdateForm(jobID)
    job = {
    'job ID': result[0][0],
    'job name': result[0][1],
    'work order': result[0][2],
    'cell': result[0][3],
    'cell ID': result[0][4],
    'status': result[0][5],
    'status ID': result[0][6],
     'type': result[0][7],
    'type ID': result[0][8],
    'weight': result[0][9],
    'activity ID' : result[0][10],
    'operator': result[0][11],
    'operator ID': result[0][12],
    'last op': result[0][13],
    'notes': result[0][14],
    'last activity': result[0][15],
    }



    return render_template('update_job.html',job=job, oplist=oplist, page=page)





@app.route("/runningjobs/", methods=['POST','GET'])
def runningJobs():
    page = "Running Jobs"
    jobList = DB.getRunningJobsList()
    jobs = []
    for job in jobList:
        jobs.append({
            'jobID':job[0],
            'job':job[1],
            'workorder':job[2],
            'cell':job[3],
            'status':job[4],
            'weight':job[5],
            'operator':job[7],
            'timestamp':job[8],})

    if request.method == 'POST':
        errors = False
        
        if not request.form['JobID']:
            errors = True

        if not errors:

            jobID = request.form['JobID']
            return redirect(url_for('updateJob', jobID=jobID))
        else:
            return render_template('runningjobs.html', jobs=jobs, page=page)

    return render_template('runningjobs.html', jobs=jobs, page=page)



@app.route("/new_job_success/", methods=['POST','GET'])
def jobSuccess():
    page = "Job Added"
    return render_template('new_job_success.html', page=page)



@app.route("/new_job/", methods=['POST','GET'])
def newJobform():
    page = 'Start Job'
    oplist = DB.getActiveOperators()
    typeList = DB.getJobType()
    workcellList = DB.getWorkCells()

    # Form handler------------------------------------ 
    if request.method == 'POST':
        errors = False

        if not request.form['operator']:
            errors = True

        if not request.form['job_name']:
            errors = True

        if not request.form['work_order']:
            errors = True

        if not request.form['work_cell']:
            errors = True

        if not request.form['job_type']:
            errors = True

        if not request.form['job_weight']:
            errors = True

        if not request.form['total_operations']:
            errors = True

        try:
            ck_ipt = request.form['in_process_testing']
        except:
            ck_ipt = '0'

        try:
            ck_pre = request.form['predjustments']
        except:
            ck_pre = '0'


        if not errors:
            now = datetime.now()
            time = now.strftime('%I:%M %p')
            date = now.strftime('%m-%d-%Y')
            newRecord = {
                'operator': request.form['operator'],
                'job': request.form['job_name'],
                'workOrder': request.form['work_order'],
                'workCell' : request.form['work_cell'],
                'jobType' : request.form['job_type'],
                'jobWeight': request.form['job_weight'],
                'totalOperatiions': request.form['total_operations'],
                'inProcessTesting': ck_ipt,
                'preAdjustments' : ck_pre,
                'notes' : request.form['notes'],
                'jobStatus' : 1, # Job status is 'In Progress' as a starting condtion (job status table)
                'startTime' : time,
                'startDate' : date,
                'lastOperation': 10, #jobs start at operation 10
                'Activity' : 4 #the value 4 represents 'starting' from the Activity_Action table
            }
            DB.startJob(newRecord)
            page = "Job Added"
            return  render_template('new_job_success.html',newRecord=newRecord, page=page)
           
        else:
            return render_template('new_job.html', oplist=oplist,typeList=typeList,workcellList=workcellList, page=page)
        

    return render_template('new_job.html', oplist=oplist,typeList=typeList,workcellList=workcellList, page=page)












if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=5000)