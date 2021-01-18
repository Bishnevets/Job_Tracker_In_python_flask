
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
