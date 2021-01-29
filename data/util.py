
from datetime import datetime
from data import DB


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