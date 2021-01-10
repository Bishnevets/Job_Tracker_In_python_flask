from data import DB



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


print(output['monthCount'])