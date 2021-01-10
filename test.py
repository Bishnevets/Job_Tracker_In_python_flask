from data import DB


jobList = DB.getRunningJobsList()
jobs = []
for job in jobList:
    jobs.append({'jobID':job[0],'job':job[1],'workorder':job[2],'cell':job[3],'status':job[4],'weight':job[5],'operator':job[6],'timestamp':job[7],})



print(jobs[5]['weight'])