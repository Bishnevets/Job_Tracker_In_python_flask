from data import DB, util
from datetime import datetime
from flask import json, jsonify



now = datetime.now()
time = now.strftime('%I:%M %p')
date = now.strftime('%m-%d-%Y')


# date = (now.strftime('%A %B %d, %Y'))







# for date in dates:
#     print(date[1])

# def formatDateForDatabase(date):
        
#         x = len(date)

#         empty = True

#         for char in date:
#             if char == '/':
#                 empty = False
#                 break

#         if not empty:
#             date = date.split('/')
#             month = str(date[0])
#             day = str(date[1])
#             year = str(date[2])

#             if len(month) == 1:
#                 month = '0' + month
            
#             if len(day) == 1:
#                 day = '0' + day

            
#             dateBuilder = year + '-' + month + '-' + day
#         else:
#             dateBuilder = ""

#         return dateBuilder


# records = DB.reformateDate_jobRecord()

# for record in records:
#     id = record[0]
#     if record[1] == None:
#         date = formatDateForDatabase(" ")
#     else:
#         date = formatDateForDatabase(record[1])
#     print(DB.updateDateField(id,date))
#     print("success")

#  print(str(formatDateForDatabase(date[1])) + " " + str(date[0]))
    
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


print(CellOBJ)


