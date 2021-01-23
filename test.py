from data import DB, util
from datetime import datetime



now = datetime.now()
time = now.strftime('%I:%M %p')
date = now.strftime('%m-%d-%Y')


# date = (now.strftime('%A %B %d, %Y'))







# for date in dates:
#     print(date[1])

def formatDateForDatabase(date):

        empty = True

        for char in date:
            if char == '/':
                empty = False
                break

        if not empty:
            date = date.split('/')
            month = str(date[0])
            day = str(date[1])
            year = str(date[2])

            
            dateBuilder = year + '-' + month + '-' + day
        else:
            dateBuilder = ""

        return dateBuilder


records = DB.reformateDate_jobRecord()

for record in records:
    id = record[0]
    date = formatDateForDatabase(record[1])
    print(DB.updateDateField(id,date))
    print("success")

#  print(str(formatDateForDatabase(date[1])) + " " + str(date[0]))
    