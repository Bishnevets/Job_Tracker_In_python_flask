from data import DB
from datetime import datetime
# x = DB.getJobType()

# for item in x:
#     print(item[0])


# now = datetime.now()
# time = now.strftime('%I:%M %p')
# date = now.strftime('%m-%d-%Y')

# d = date + ' ' + time

# print(d)




now = datetime.now()
time = now.strftime('%I:%M %p')
date = now.strftime('%m-%d-%Y')
newRecord = {
    'operator': 1,
    'job': "x-test",
    'workOrder': "123",
    'workCell' : 1,
    'jobType' : 1,
    'jobWeight': "25",
    'totalOperatiions': 20,
    'inProcessTesting': 1,
    'preAdjustments' : 0,
    'notes' : "",
    'jobStatus' : 1, # Job status is 'In Progress' as a starting condtion (job status table)
    'startTime' : time,
    'startDate' : date,
    'lastOperation': 10, #jobs start at operation 10
    'Activity' : 4 #the value 4 represents 'starting' from the Activity_Action table
}

DB.startJob(newRecord)



