from data import DB

x = DB.getJobType()

for item in x:
    print(item[0])