from data import DB, util
from datetime import datetime
from flask import json, jsonify


now = datetime.now()
time = now.strftime('%I:%M %p')
date = now.strftime('%m-%d-%Y')

# date = (now.strftime('%A %B %d, %Y'))


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



print(typeCountSet['year'])
print(typeCountYear)

