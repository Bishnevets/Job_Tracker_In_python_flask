# from flask_sqlalchemy import SQLAlchemy
import sqlite3
import csv
import data.SQL as Q

def make_connection():
    connection_String = "C:\\Users\\sbish\\Desktop\\project x\\data\\JT_DATA.db" #home
    #connection_String = "C:\\Users\\stephenb\\Desktop\\project x\\data\\JT_DATA.db" #work
    return sqlite3.connect(connection_String)

def end_connection(conn):
    conn.close()

def getActiveOperators():    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectActiveOperators()
    c.execute(SQL)
    items = c.fetchall()
    end_connection(conn)
    return items
    
def getWorkCells():    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectWorkCells()
    c.execute(SQL)
    items = c.fetchall()
    end_connection(conn)
    return items

def getJobType():    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectJobType()
    c.execute(SQL)
    items = c.fetchall()
    end_connection(conn)
    return items

def startJob(newRecord):
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.InsertIntoJobRecord(newRecord)
    c.execute(SQL)
    conn.commit()
    SQL = Q.SelectLastJobRecord()
    c.execute(SQL)
    JobIndex = c.fetchone()[0]
    SQL = Q.InsertIntoActivity(newRecord,JobIndex)
    c.execute(SQL)
    conn.commit()
    end_connection(conn)

def getLastJobRecord():
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectLastJobRecord()
    c.execute(SQL)
    value = c.fetchone()[0]
    end_connection(conn)
    return value

def RunningJobsCount():
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectRunningJobsCount()
    c.execute(SQL)
    value = c.fetchone()[0]
    end_connection(conn)
    return value

def getJobsCompleteToday():
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectCompleteTodayCount()
    c.execute(SQL)
    value = c.fetchone()[0]
    end_connection(conn)
    return value

def getJobsCompleteThisWeek():
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectCompleteThisWeekCount()
    c.execute(SQL)
    value = c.fetchone()[0]
    end_connection(conn)
    return value

def getJobsCompleteThisMonth():
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectCompleteThisMonthCount()
    c.execute(SQL)
    value = c.fetchone()[0]
    end_connection(conn)
    return value











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

