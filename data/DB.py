# from flask_sqlalchemy import SQLAlchemy
import sqlite3
import csv
import data.SQL as Q

def make_connection():
    #connection_String = "C:\\Users\\sbish\\Desktop\\project x\\data\\JT_DATA.db" #home
    connection_String = "C:\\Users\\stephenb\\Desktop\\project x\\data\\JT_DATA.db" #work

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
    SQL = Q.InsertInitnialActivity(newRecord,JobIndex)
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


def getRunningJobsList():    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectRunningJobList()
    c.execute(SQL)
    items = c.fetchall()
    end_connection(conn)
    return items


def getCompletedJobsList(query_type):    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectCompletedJobList(query_type)
    c.execute(SQL)
    items = c.fetchall()
    end_connection(conn)
    return items



def getOperatorByID(id):    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectOperatorByID(id)
    c.execute(SQL)
    value = c.fetchone()[0]
    end_connection(conn)
    return value


def getFinalOperationByID(id):    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectFinalOperation(id)
    c.execute(SQL)
    value = c.fetchone()[0]
    end_connection(conn)
    return value




def getStatusByID(id):    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectStatusById(id)
    c.execute(SQL)
    value = c.fetchone()[0]
    end_connection(conn)
    return value



def setUpdateForm(JobID):
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectJobToUpdate(JobID)
    c.execute(SQL)
    items = c.fetchall()
    end_connection(conn)
    return items


def logActivity(details):
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.InsertActivity(details)
    c.execute(SQL)
    conn.commit()
    end_connection(conn)
    

def updateJobRecord(details):
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.UpdateJobRecord(details)
    c.execute(SQL)
    conn.commit()
    end_connection(conn)
    return SQL


def updateJobNotes(details):
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.UpdateJobNotes(details)
    c.execute(SQL)
    conn.commit()
    end_connection(conn)
    return SQL


def getTodaysCellCount():
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectCompleteByWorkCellDaily()
    c.execute(SQL)
    items = c.fetchall()
    end_connection(conn)
    return items



def getCellCountAggregets():
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.selectCountAggregates()
    c.execute(SQL)
    items = c.fetchall()
    end_connection(conn)
    return items



def getReport():    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectNightlyReportQuerey()
    c.execute(SQL)
    items = c.fetchall()
    end_connection(conn)
    return items



def getJobTypeCount(routing):    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectJobTypeCount(routing)
    c.execute(SQL)
    items = c.fetchone()
    end_connection(conn)
    return items




#------------------------------------SPECIAL Functions----------------------------------------------------------

def reformateDate_jobRecord(query):
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.selectDateToUpdate(query)
    c.execute(SQL)
    items = c.fetchall()
    return items


    
def updateDateField(record, date, query):
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.updateDateFormat(record, date, query)
    c.execute(SQL)
    conn.commit()
    end_connection(conn)
    return SQL





def getNoteStringLength(id):    
    conn = make_connection()
    c = conn.cursor()
    SQL = Q.SelectNotesByID(id)
    c.execute(SQL)
    items = c.fetchall()[0][0]
    end_connection(conn)
    return items







# -------------------------------------DB PARTS---------------------------------------------

#  conn = make_connection()
#    SQL = ""
#    c.execute(SQL)
#    conn.commit()
#    end_connection(conn)




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

