# from flask_sqlalchemy import SQLAlchemy
import sqlite3
import csv

def make_connection():
    connection_String = "C:\\Users\\sbish\\Desktop\\project x\\data\\JT_DATA.db" #home
    #connection_String = "C:\\Users\\stephenb\\Desktop\\project x\\data\\JT_DATA.db" #work
    return sqlite3.connect(connection_String)

def end_connection(conn):
    conn.close()



def getActiveOperators():    
    conn = make_connection()
    c = conn.cursor()
    SQL = "SELECT "
    SQL += "o.Operator_ID, "
    SQL += "o.First_Name || ' ' || o.Last_Name AS [Name], "
    SQL += "ds.Shift, "
    SQL += "os.Status "
    SQL += "FROM Operators o "
    SQL += "JOIN Dept_Shifts ds ON ds.Shift_ID = o.Shift "
    SQL += "JOIN Operator_Status os ON os.Status_ID = o.Status "
    SQL += "WHERE os.Status NOT IN ('Inactive') "
    SQL += "ORDER BY ds.Shift, [Name]"

    c.execute(SQL)
    items = c.fetchall()

    # for item in items:
    #     print(str(item[1]))

    end_connection(conn)

    return items
    


def getWorkCells():    
    conn = make_connection()
    c = conn.cursor()
    SQL = "SELECT "
    SQL += "wc.Cell_ID, "
    SQL += "wc.Cell  "
    SQL += "FROM Work_Cells wc; "
    

    c.execute(SQL)
    items = c.fetchall()

    # for item in items:
    #     print(str(item[1]))

    end_connection(conn)

    return items


    
def getJobType():    
    conn = make_connection()
    c = conn.cursor()
    SQL = "SELECT "
    SQL += "jc.Type_ID, "
    SQL += "jc.Type "
    SQL += "FROM Job_Categories jc; "
    

    c.execute(SQL)
    items = c.fetchall()

    # for item in items:
    #     print(str(item[1]))

    end_connection(conn)

    return items


def startJob(newRecord):
    conn = make_connection()
    c = conn.cursor()


    oper  = newRecord['operator']
    job   = newRecord['job']
    WO    = newRecord['workOrder']
    cell  = newRecord['workCell']
    jtype = newRecord['jobType']
    weig  = newRecord['jobWeight']
    tops  = newRecord['totalOperatiions']
    test  = newRecord['inProcessTesting']
    PA    = newRecord['preAdjustments']
    note  = newRecord['notes']
    stat  = newRecord['jobStatus']
    time  = newRecord['startTime']
    date  = newRecord['startDate']
    last  = newRecord['lastOperation']
    acti  = newRecord['Activity']

    SQL = "INSERT INTO Job_Record ( "
    SQL += "Job, "
    SQL += "Work_Order, "
    SQL += "Job_Weight, "
    SQL += "Work_Cell, "
    SQL += "Job_Type, "
    SQL += "Job_Status, "
    SQL += "Start_Time, "
    SQL += "Notes, "
    SQL += "'In-Process_Testing', "
    SQL += "Pre_Adjustment, "
    SQL += "Total_Operations, "
    SQL += "Start_Date, "
    SQL += "Last_Operation) "
    SQL += "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);"
    c.execute(SQL,(job,WO,weig,cell,jtype,stat,time,note,test,PA,tops,date,last))
    conn.commit()
    

    SQL = "SELECT Max(Job_ID) FROM Job_Record jr;"
    c.execute(SQL)
    JobIndex = c.fetchone()[0]


    SQL = "INSERT INTO Activity( "
    SQL += "Operator, " 
    SQL += "Activity, "
    SQL += "Activity_Date, "
    SQL += "Job_Id, "
    SQL += "Operation, " 
    SQL += "Activity_Time) "
    SQL += "VALUES(?,?,?,?,?,?);"
    c.execute(SQL,(oper,acti,date,JobIndex,last,time))
    conn.commit()

    end_connection(conn)
    message = "Job Started"
    # return message




def getLastJobRecord():
    conn = make_connection()
    c = conn.cursor()
    SQL = "SELECT Max(Job_ID) FROM Job_Record jr;"
    c.execute(SQL)
    value = c.fetchone()[0]
    end_connection(conn)
    return value










# getActiveOperators()
# getWorkCells()
# getJobType()


























# -------------------------------------DB PARTS---------------------------------------------

#  conn = make_connection()
#    SQL = ""
#    c.execute(SQL)
#    conn.commit()
#    end_connection(conn)



   
    # conn = make_connection()
    # c = conn.cursor()
    # SQL = ""
    #SQL += ""
    # c.execute(SQL)
    # items = c.fetchall()
    # for item in items:
    #     print(str(item))
    # end_connection(conn)



    # def add_one(first,last,email):
#     conn = make_connection()
#     c = conn.cursor()

#     SQL = "INSERT INTO customers "
#     SQL += "(first_name, last_name, email) "
#     SQL += "VALUES(?,?,?);" #placeholder method

#     c.execute(SQL,(first,last,email))
#     conn.commit()
#     end_connection(conn)



# def export():
#     conn = make_connection()
#     c = conn.cursor()
#     outfile = open('dumpfile.csv','w',newline="")
#     outcsv = csv.writer(outfile)
#     c.execute("SELECT * FROM customers")
#     outcsv.writerow(x[0] for x in c.description)
#     outcsv.writerows(c.fetchall())
#     outfile.close()
#     end_connection(conn)

