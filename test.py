from data import DB, util
from datetime import datetime

now = datetime.now()
time = now.strftime('%I:%M %p')
date = now.strftime('%m-%d-%Y')



# def appendTimeStamp(user,appendTo, message="Log Entry"):

#             now = datetime.now()
#             time = now.strftime('%I:%M %p')
#             date = now.strftime('%m-%d-%Y')   
#             stamp = "\n***" + message + " " + time + " " + date + "\n"
#             stamp += "------------------------" + user + "\n"
#             return  appendTo + stamp


# alias = util.getUserAlias('12')
# notes = "This is what happened"
# x =util.appendTimeStamp(alias,notes)





# x =appendTimeStamp('SBishop','Job')



x =  DB.getNoteStringLength(718)
y = DB.getNoteStringLength(718)
print(util.compareAreaTextSize(x,y))

# print(DB.getNoteStringLength(200))


'Log Entry 10:25 PM 01-15-2021\r\n------------------------TCassese\r\n\r\n\r\nLog Entry 10:30 PM 01-15-2021\r\n------------------------TCassese\r\n\nLog Entry 10:31 PM 01-15-2021\n------------------------TCassese\n'
'Log Entry 10:25 PM 01-15-2021\r\n------------------------TCassese\r\n\r\n\r\nLog Entry 10:30 PM 01-15-2021\r\n------------------------TCassese\r\n\r\nLog Entry 10:31 PM 01-15-2021\r\n------------------------TCassese\r\n'