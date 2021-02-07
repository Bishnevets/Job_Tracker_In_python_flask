
from datetime import datetime
from data import DB
import csv


def getUserAlias(id):
    user = DB.getOperatorByID(id)
    delimIndex = user.index(" ")
    substr_1 = user[0]
    substr_2 = user[delimIndex + 1:]
    user_alias = substr_1+substr_2
    return  user_alias


def appendTimeStamp(user,appendTo,message="Log Entry"):
    now = datetime.now()
    time = now.strftime('%I:%M %p')
    date = now.strftime('%m-%d-%Y')   
    stamp = "\n\n" + message + " " + time + " " + date + "\n"
    stamp += "----------------------------------" + user + "\n"
    return  appendTo + stamp




def textHasChanged(val_1,val_2):
    
    val_1 = str(val_1)
    val_1 = val_1.replace('\n','')
    val_1 = val_1.replace('\r','')

    x = len(val_1)

    val_2 = str(val_2)
    val_2 = val_2.replace('\n','')
    val_2 = val_2.replace('\r','')

    y = len(val_2)

    if val_1 == val_2:
        return False
    else:
        return True








def formatDateForDatabase(date):
        x = len(date)

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

            if len(month) == 1:
                month = '0' + month
            
            if len(day) == 1:
                day = '0' + day

            dateBuilder = year + '-' + month + '-' + day
        else:
            dateBuilder = ""

        return dateBuilder



def fixDatabaseDate():
    records = DB.reformateDate_jobRecord(1)

    for record in records:
        id = record[0]
        if record[1] == None:
            date = formatDateForDatabase(" ")
        else:
            date = formatDateForDatabase(record[1])
        print(DB.updateDateField(id,date,1))
        print("success")

    records = DB.reformateDate_jobRecord(2)
    for record in records:
        id = record[0]
        if record[1] == None:
            date = formatDateForDatabase(" ")
        else:
            date = formatDateForDatabase(record[1])
        print(DB.updateDateField(id,date,2))
        print("success")

    records = DB.reformateDate_jobRecord(3)
    for record in records:
        id = record[0]
        if record[1] == None:
            date = formatDateForDatabase(" ")
        else:
            date = formatDateForDatabase(record[1])
        print(DB.updateDateField(id,date,3))
        print("success")



#This is for the Jobs complete page
def setPageMessage(var):
    heading = "JOBS COMPLETE: "
    value = var
    if var.split(',')[0] == 'range':
        if var.split(',')[1] == var.split(',')[2]:
            value = var.split(',')[1]
        else:
            value = var.split(',')[1]
            value += " - "
            value += var.split(',')[2]

    if var == 'month' or var == 'week':
        value = "this " + var

    return heading + value.upper()





    #returns a list of job operations starting with the last recorded
    #and advancing through 90 which is the last availble operation
    #operations increment in incremnts of 10

def getAvailableOperationValues(last_op):
    max_value = 90
    value = int(last_op)
    val_list = []
    while value <= max_value:
        val_list.append(value)
        value += 10
    return val_list






def runNightReport():
    now = datetime.now()
    time = now.strftime('%I-%M-%p')
    date = now.strftime('%m-%d-%Y')

    path = "S:\\EVERYONE\\SBishop\\Job Tracker Admin\\Reports"
    reportTemplate = []
    reportHeadings = ['Name', 'Job', 'Work Order', 'Work Cell', 'Job Type', 'Status', 'weight', 'Notes' ]
    reportRaw = DB.getReport()
    reportTemplate.append(reportHeadings)
    for each in reportRaw:
        reportTemplate.append([each[0],each[1],each[2],each[3],each[4],each[5],each[6],each[9]])

    filename = "\\NightlyChemOpReport-" + str(date) + "-" + str(time) + ".csv"


    outfile = open( path + filename,"w",newline="")
    outcsv =csv.writer(outfile)
    outcsv.writerows(reportTemplate)
    outfile.close()

