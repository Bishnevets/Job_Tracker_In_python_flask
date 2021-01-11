from data import DB


result = DB.setUpdateForm(687)

job = {
    'job ID': result[0][0],
    'job name': result[0][1],
    'work order': result[0][2],
    'cell': result[0][3],
    'cell ID': result[0][4],
    'status': result[0][5],
    'status ID': result[0][6],
     'type': result[0][7],
    'type ID': result[0][8],
    'weight': result[0][9],
    'activity ID' : result[0][10],
    'operator': result[0][11],
    'operator ID': result[0][12],
    'last op': result[0][13],
    'notes': result[0][14],
    'last activity': result[0][15],
}

print(job)


