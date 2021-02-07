from flask import Flask, render_template, request, redirect, jsonify, json
from markupsafe import escape
import os
import csv
from data import DB, util
from datetime import datetime
from flask.helpers import url_for
import calendar


# web application instance
app = Flask(__name__)


#----------------------------------------lists and veriables--------------------------------------------- 







#============================================== ROUTING SECTION =========================================



# DASHBOARD ROUTE =======================================================================================
@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/dashboard", methods=["GET", "POST"])
def index():

    page = "THE DASHBOARD"
    now = datetime.now()
    today = now.strftime('%A %B %d, %Y')
    runningJobs = DB.RunningJobsCount()
    dayCount = DB.getJobsCompleteToday()
    weekCount = DB.getJobsCompleteThisWeek()
    monthCount = DB.getJobsCompleteThisMonth()


    typeCountSet = {
        'day':[0,0,0],
        'week':[0,0,0],
        'month':[0,0,0],
        'year':[0,0,0]
    }

    typeCountDay = []            
    typeCountSet['day'][0] = DB.getJobTypeCount(0)[0]
    typeCountSet['day'][1] = DB.getJobTypeCount(1)[0]
    typeCountSet['day'][2] = DB.getJobTypeCount(2)[0]
    for each in typeCountSet['day']:
        typeCountDay.append(each)

    typeCountWeek = []  
    typeCountSet['week'][0] = DB.getJobTypeCount(3)[0]
    typeCountSet['week'][1] = DB.getJobTypeCount(4)[0]
    typeCountSet['week'][2] = DB.getJobTypeCount(5)[0]
    for each in typeCountSet['week']:
        typeCountWeek.append(each)

    typeCountMonth = []  
    typeCountSet['month'][0] = DB.getJobTypeCount(6)[0]
    typeCountSet['month'][1] = DB.getJobTypeCount(7)[0]
    typeCountSet['month'][2] = DB.getJobTypeCount(8)[0]
    for each in typeCountSet['month']:
        typeCountMonth.append(each)

    typeCountYear = []  
    typeCountSet['year'][0] = DB.getJobTypeCount(9)[0]
    typeCountSet['year'][1] = DB.getJobTypeCount(10)[0]
    typeCountSet['year'][2] = DB.getJobTypeCount(11)[0]
    for each in typeCountSet['year']:
        typeCountYear.append(each)





# Bar Chart=========================================
    CellOBJ = {
        "Large Hock": 0,
        "Pilot Hock": 0,
        "2 Gal Ross": 0,
        "10 Gal Ross": 0,
        "40 Gal Ross": 0,
        "100 Gal Ross": 0,
        "Mezz Tank": 0,
        "Activator": 0,
        "1/2 Gal Ross": 0,
    }

    cellcount = DB.getTodaysCellCount()
    for cell in cellcount:
     CellOBJ[cell[0]] = cell[1]
     print(CellOBJ[cell[0]])

    cellData = [CellOBJ["Pilot Hock"],
                CellOBJ["Large Hock"],
                CellOBJ["1/2 Gal Ross"],
                CellOBJ["2 Gal Ross"],
                CellOBJ["10 Gal Ross"],
                CellOBJ["40 Gal Ross"],
                CellOBJ["100 Gal Ross"],
                CellOBJ["Mezz Tank"],
                CellOBJ["Activator"]]
# Bar Chart =========================================



    output = {
        'runningJobs' : runningJobs,
        'dayCount' : dayCount,
        'weekCount' : weekCount,
        'monthCount' : monthCount
    }

    return render_template('index.html', 
                            output=output, 
                            page=page, 
                            today=today,
                            cellData = json.dumps(cellData),
                            typeCountDay = json.dumps(typeCountDay),
                            typeCountWeek = json.dumps(typeCountWeek),
                            typeCountMonth = json.dumps(typeCountMonth),
                            typeCountYear = json.dumps(typeCountYear)    
                            )
# ======================================================================================== DASHBOARD ROUTE







# RUNNING JOBS ROUTE ====================================================================================


@app.route("/runningjobs/", methods=['POST','GET'])
def runningJobs():
    page = "WORK IN PROCESS"
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
# ===================================================================================== RUNNING JOBS ROUTE






# COMPLETED JOBS ROUTE ===================================================================================
@app.route("/completed_jobs/", methods=['POST','GET'])
@app.route("/completed_jobs/<query_type>", methods=['POST','GET'])

def completedJobs(query_type = 'all'):
    page = util.setPageMessage(query_type)
    jobList = DB.getCompletedJobsList(query_type)
    jobCount = len(jobList)
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
            return redirect(url_for('viewComplete', jobID=jobID))
        else:
            return render_template('completed_jobs.html', jobs=jobs, page=page, jobCount=jobCount)

    return render_template('completed_jobs.html', jobs=jobs, page=page, jobCount=jobCount)
#  =================================================================================== COMPLETED JOBS ROUTE



# TEST LAND ROUTE ===========================================================================================
@app.route("/test_land/", methods=['POST','GET'])
def testland():
    page = "TEST POSTED"
    query_type = " "
    if request.method == 'POST':
        query_type = request.form['query-type']
        return redirect(url_for('completedJobs', query_type=query_type))
       
    return render_template('test_land.html', page=page, query_type=query_type)
# =========================================================================================== TEST LAND ROUTE

# RANGE SEARCH ROUTE ===========================================================================================
@app.route("/range_search/", methods=['POST','GET'])
def rangeSearch():
    page = "RANGE TEST"
    range_1 = " "
    range_2 = " "
    if request.method == 'POST':
        range_1 = request.form['start_range']
        range_2 = request.form['end_range']
        query_type = request.form['query-type']

        query_type += "," + range_1 + "," + range_2
        return redirect(url_for('completedJobs', query_type=query_type))
      
       
    return render_template('range_search.html', page=page, query_type=query_type)
# =========================================================================================== TEST LAND ROUTE









# NEW JOBS ROUTE ===========================================================================================
@app.route("/new_job/", methods=['POST','GET'])
def newJobform():
    page = 'START A NEW JOB'
    oplist = DB.getActiveOperators()
    typeList = DB.getJobType()
    workcellList = DB.getWorkCells()


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
            date = now.strftime('%Y-%m-%d')

            alias = util.getUserAlias(request.form['operator'])
            notes = request.form['notes']
            addNote = util.appendTimeStamp(alias,notes,'Job Started')


            newRecord = {
                'operator': request.form['operator'],
                'job': request.form['job_name'].upper(),
                'workOrder': request.form['work_order'],
                'workCell' : request.form['work_cell'],
                'jobType' : request.form['job_type'],
                'jobWeight': request.form['job_weight'],
                'totalOperatiions': request.form['total_operations'],
                'inProcessTesting': ck_ipt,
                'preAdjustments' : ck_pre,
                'notes' : addNote,
                'jobStatus' : 1, # Job status is 'In Progress' as a starting condtion (job status table)
                'startTime' : time,
                'startDate' : date,
                'lastOperation': 10, #jobs start at operation 10
                'Activity' : 4 #the value 4 represents 'starting' from the Activity_Action table
            }


            DB.startJob(newRecord)
            page = "JOB ADDED"


            newRecord['operator'] = DB.getOperatorByID(newRecord['operator'])

           

            #return redirect(url_for('index'))
            return  render_template('new_job_success.html',newRecord=newRecord, page=page)
           
        else:
            return render_template('new_job.html', oplist=oplist,typeList=typeList,workcellList=workcellList, page=page)
        

    return render_template('new_job.html', oplist=oplist,typeList=typeList,workcellList=workcellList, page=page)
# ================================================================================================= NEW JOBS ROUTE 






# ADD JOB SUCCESS ROUTE ===========================================================================================
@app.route("/new_job_success/", methods=['POST','GET'])
def jobSuccess():
    page = "NEW JOB ADDED"
    return render_template('new_job_success.html', page=page)
# =========================================================================================== ADD JOB SUCCESS ROUTE








# UPDATE JOB ROUTE ===========================================================================================
@app.route("/update_job/<jobID>", methods=["GET", "POST"])
def updateJob(jobID):
    page = "UPDATE WORK IN PROCESS"
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

    operationValues = util.getAvailableOperationValues(job['last op'])
    # #to be passed to the next operation combo box
    

    errors = True
    
    
    if request.method == 'POST':
        errors = False
        
        if not request.form['action']:
            errors = True
            
        if not request.form['operator']:
            errors = True
            
        if not request.form['next-operation']:
            errors = True
            

        if not errors:



            now = datetime.now()
            time = now.strftime('%I:%M %p')
            date = now.strftime('%Y-%m-%d')
            dbNotes = job['notes']
            pageNotes = request.form['notes']
            OperatorID = request.form['operator']
            nextOperation = request.form['next-operation']
            action = request.form['action']
            status = action

            if action == "7":
                status = 1

            if action == "2":
                nextOperation = DB.getFinalOperationByID(job['job ID'])
                alias = util.getUserAlias(OperatorID)
                notes = pageNotes
                addNote = util.appendTimeStamp(alias,notes,'Job Completed')
                
                
            # Note Handling
            if(util.textHasChanged(dbNotes,pageNotes)):
                alias = util.getUserAlias(OperatorID)
                notes = pageNotes
                if action == "2":
                    addNote = util.appendTimeStamp(alias,notes,'Job Completed')
                else:
                    addNote = util.appendTimeStamp(alias,notes)
            else:
                if action == "2":
                    alias = util.getUserAlias(OperatorID)
                    addNote = util.appendTimeStamp(alias,dbNotes,'Job Completed')
                else:
                    addNote = dbNotes
           
            details = {
                'jobID': job['job ID'],
                'status': status,
                'activity': action,
                'notes' : addNote,
                'time' : time,
                'date' : date,
                'operation' : nextOperation,
                'operator' : request.form['operator']
            }

            DB.logActivity(details)
            if not(request.form['action'] == '2') and not(request.form['action'] == '5'):
                time = ''
                date = ''
            
            DB.updateJobRecord(details)

            details['job'] = job['job name']
            details['work order'] = job['work order']
            details['operator'] = DB.getOperatorByID(details['operator'])
            details['status'] = DB.getStatusByID(details['status'])
           

            page = "UPDATE SUCCESS"
            return render_template('update_job_success.html',details=details, page=page)
        
        #return redirect(url_for('index'))

    else:
        return render_template('update_job.html',job=job, oplist=oplist, page=page, operationValues=operationValues)

    return render_template('update_job.html',job=job, oplist=oplist, page=page, operationValues=operationValues)
# =========================================================================================== UPDATE JOB ROUTE




# JOB UPDATE SUCCESS ROUTE ===========================================================================================

@app.route("/update_job_success/", methods=['POST','GET'])
def updateJobSuccess():
    page = "UPDATE SUCCESSFUL"

    return render_template('update_job_success.html', page=page)
# =========================================================================================== JOB UPDATE SUCCESS ROUTE





# VIEW JOB RECORD ROUTE ===========================================================================================
@app.route("/job_record/<jobID>", methods=["GET", "POST"])
def viewComplete(jobID):
   
    page = "JOB RECORD"
    oplist = DB.getActiveOperators()
    typeList = DB.getJobType()
    workcellList = DB.getWorkCells()
    result = DB.setUpdateForm(jobID)
    endDate = result[0][15]
    endDate = endDate[0:10]

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
    'last activity': endDate
    }

    if request.method == 'POST':        
        now = datetime.now()
        time = now.strftime('%I:%M %p')
        date = now.strftime('%Y-%m-%d')
        dbNotes = job['notes']
        pageNotes = request.form['notes']


        if(util.textHasChanged(dbNotes,pageNotes)):
            alias = "SYS"
            notes = pageNotes
            addNote = util.appendTimeStamp(alias,notes)
        else:
            addNote = dbNotes

        
        details = {
                'jobID': job['job ID'],
                'notes' : addNote
                }
                
        DB.updateJobNotes(details)
           

        return redirect(url_for('completedJobs'))

    else:
        return render_template('job_record.html',job=job, oplist=oplist, page=page)

    return render_template('job_record.html',job=job, oplist=oplist, page=page)
# =========================================================================================== VIEW JOB RECORD ROUTE



# NIGHTLY REPORTS  ===========================================================================================
@app.route("/report/", methods=['POST','GET'])
def report():
    page = "Nightly REPORT"

    util.runNightReport()

    return render_template('report.html', page=page)


#   =========================================================================================== NIGHTLY REPORTS



# RUN PROGRAM ===========================================================================================

if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=5000)
