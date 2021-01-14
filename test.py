from data import DB
from datetime import datetime



now = datetime.now()
time = now.strftime('%I:%M %p')
date = now.strftime('%m-%d-%Y')
            
details = {
    'jobID': '687',
    'status': '2',
    'activity':'2',
    'notes' : 'this is working',
    'time' : '',
    'date' : '',
    'operation' : '34',
    'operator' : '7'
}

# DB.logActivity(details)
print(DB.updateJobRecord(details))


