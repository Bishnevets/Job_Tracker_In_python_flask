
# -----------------------------------SELECT SATEMENTS-----------------------------------------------------------


def SelectRunningJobsCount():
    SQL = "SELECT Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr WHERE jr.Job_Status  in (1,3,4,7)"
    return SQL


def SelectCompleteTodayCount():
    SQL = "SELECT Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr " 
    SQL += "WHERE jr.Job_Status = 2 AND jr.End_Date  = DATE('now','localtime');"
    return SQL


def SelectCompleteThisWeekCount():
    SQL = "SELECT Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr " 
    SQL += "WHERE jr.Job_Status = 2 AND jr.End_Date  >= date('now','localtime', 'weekday 1', '-7 days');"
    return SQL


def SelectCompleteThisMonthCount():
    SQL = "SELECT Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr " 
    SQL += "WHERE jr.Job_Status = 2 AND jr.End_Date  >= date('now','localtime','start of month');"
    return SQL


def  SelectLastJobRecord():
    SQL = "SELECT Max(Job_ID) FROM Job_Record jr;"
    return SQL

def SelectJobType():    
    SQL = "SELECT jc.Type_ID, jc.Type FROM Job_Categories jc; "
    return SQL

def SelectWorkCells():    
    SQL = "SELECT wc.Cell_ID, wc.Cell FROM Work_Cells wc; "
    return SQL


def SelectOperatorByID(id):
     SQL = "SELECT o.First_Name || ' ' || o.Last_Name AS [Name] FROM Operators o Where o.Operator_ID = '" + str(id) + "'"
     return SQL

def SelectNotesByID(id):
    SQL = "SELECT Notes FROM Job_Record jr WHERE jr.Job_ID = '" + str(id) + "'"
    return SQL

def SelectActiveOperators():
    SQL = "SELECT o.Operator_ID, o.First_Name || ' ' || o.Last_Name AS [Name], ds.Shift, os.Status "
    SQL += "FROM Operators o "
    SQL += "JOIN Dept_Shifts ds ON ds.Shift_ID = o.Shift "
    SQL += "JOIN Operator_Status os ON os.Status_ID = o.Status "
    SQL += "WHERE os.Status NOT IN ('Inactive') "
    SQL += "ORDER BY ds.Shift, [Name]"
    return SQL


def SelectRunningJobList():
    SQL = "SELECT jr.Job_ID, jr.Job, jr.Work_Order, wc.Cell, js.Status, Job_Weight AS [Weight], "
    SQL += "MAX(a.Activity_ID) AS [Activity ID], o.First_Name || ' '|| o.Last_Name AS [Current Operator], "
    SQL += "a.Activity_Date ||' '|| a.Activity_Time AS [Last Activity] "
    SQL += "FROM Job_Record jr JOIN Activity a on a.Job_Id = jr.Job_ID "
    SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
    SQL +=  "JOIN Job_Status js ON js.Status_ID = jr.Job_Status "
    SQL +=  "JOIN Operators o On a.Operator = o.Operator_ID " 
    SQL += "WHERE jr.Job_Status IN (1,3,7) "
    SQL += "GROUP BY a.Job_Id;" 
    return SQL


def SelectCompletedJobList():
    SQL = "SELECT jr.Job_ID, jr.Job, jr.Work_Order, wc.Cell, js.Status, Job_Weight AS [Weight], "
    SQL += "MAX(a.Activity_ID) AS [Activity ID], o.First_Name || ' '|| o.Last_Name AS [Current Operator], "
    SQL += "jr.End_Date || ' ' || jr.End_Time AS [Completed On]"
    SQL += "FROM Job_Record jr JOIN Activity a on a.Job_Id = jr.Job_ID "
    SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
    SQL +=  "JOIN Job_Status js ON js.Status_ID = jr.Job_Status "
    SQL +=  "JOIN Operators o On a.Operator = o.Operator_ID " 
    SQL += "WHERE jr.Job_Status IN (2) "
    SQL += "GROUP BY a.Job_Id ORDER BY jr.End_Date DESC;" 
    return SQL



def SelectJobToUpdate(jobID):

    jobID = str(jobID)
    SQL = "SELECT "
    SQL += "jr.Job_ID, "
    SQL += "jr.Job, "
    SQL += "jr.Work_Order, "
    SQL += "wc.Cell, "
    SQL += "jr.Work_Cell, "
    SQL += "js.Status, "
    SQL += "jr.Job_Status, "
    SQL += "jc.'Type', "
    SQL += "jr.Job_Type, "
    SQL += "Job_Weight, "
    SQL += "MAX(a.Activity_ID) AS [Activity ID], "
    SQL += "o.First_Name || ' '|| o.Last_Name AS [Current Operator], "
    SQL += "o.Operator_ID, "
    SQL += "a.Operation, "
    SQL += "jr.Notes, "
    SQL += "a.Activity_Date ||' '|| a.Activity_Time AS [Last Activity] "
    SQL += "FROM Job_Record jr "
    SQL += "JOIN Activity a on a.Job_Id = jr.Job_ID "
    SQL += "JOIN Job_Categories jc on jc.Type_ID = jr.Job_Type "
    SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
    SQL += "JOIN Job_Status js ON js.Status_ID = jr.Job_Status "
    SQL += "JOIN Operators o On a.Operator = o.Operator_ID " 
    SQL += "WHERE jr.Job_ID = ('" + jobID + "'); "
    return SQL


# -----------------------------------INSERT STATEMENTS-----------------------------------------------------------


def InsertIntoJobRecord(newRecord):

    job   = str(newRecord['job'])
    WO    = str(newRecord['workOrder'])
    weig  = str(newRecord['jobWeight'])
    cell  = str(newRecord['workCell'])
    jtype = str(newRecord['jobType'])
    stat  = str(newRecord['jobStatus'])
    time  = str(newRecord['startTime'])
    note  = str(newRecord['notes'])
    test  = str(newRecord['inProcessTesting'])
    PA    = str(newRecord['preAdjustments'])
    tops  = str(newRecord['totalOperatiions'])
    date  = str(newRecord['startDate'])
    last  = str(newRecord['lastOperation'])

    SQL = "INSERT INTO Job_Record (Job, Work_Order, Job_Weight, Work_Cell, Job_Type, Job_Status, "
    SQL += "Start_Time, Notes, 'In-Process_Testing', Pre_Adjustment, Total_Operations, Start_Date, Last_Operation) "
    SQL += "VALUES( '" 
    SQL += job + "', '" + WO + "', '" + weig + "', '" + cell + "', '" + jtype + "', '" + stat + "', '" + time + "', '" 
    SQL += note + "', '" + test + "', '" + PA + "', '" + tops + "', '" + date + "', '" + last + "');"
    return SQL



def InsertInitnialActivity(newRecord,JobIndex):

    oper  = str(newRecord['operator'])
    acti  = str(newRecord['Activity'])
    date  = str(newRecord['startDate'])
    last  = str(newRecord['lastOperation'])
    time  = str(newRecord['startTime'])
    JobIndex = str(JobIndex)

    SQL = "INSERT INTO Activity(Operator, Activity, Activity_Date, Job_Id, Operation, Activity_Time) "
    SQL += "VALUES( '" 
    SQL += oper + "', '" + acti + "', '" + date + "', '" + JobIndex + "', '" + last + "', '" + time +"');"
    return SQL



def InsertActivity(details):

    ID    = str(details['jobID'])
    oper  = str(details['operator'])
    acti  = str(details['activity'])
    date  = str(details['date'])
    last  = str(details['operation'])
    time  = str(details['time'])

    SQL = "INSERT INTO Activity(Operator, Activity, Activity_Date, Job_Id, Operation, Activity_Time) "
    SQL += "VALUES( '" 
    SQL += oper + "', '" + acti + "', '" + date + "', '" + ID + "', '" + last + "', '" + time +"');"
    return SQL


# -----------------------------------UPDATE STATEMENTS-----------------------------------------------------------

def UpdateJobRecord(details):

    ID    = str(details['jobID'])
    status = str(details['status'])
    notes = str(details['notes'])
    endTime = str(details['time'])
    endDate = str(details['date'])
    lastOperation = str(details['operation'])

    SQL = "UPDATE Job_Record "
    SQL += "SET Job_Status='" + status + "', Notes='" + notes + "', End_Time='" + endTime + "', " 
    SQL += "End_Date='" + endDate + "', Last_Operation='" + lastOperation + "' "
    SQL += "WHERE Job_ID='" + ID + "';"
    return SQL

# -----------------------------------DELETE STATEMENTS-----------------------------------------------------------

#------------------------------------SPECIAL STATEMENTS----------------------------------------------------------

def selectDateToUpdate():
       # SQL = "SELECT Job_ID, Start_Date from Job_Record jr"
        SQL = "SELECT Job_ID, End_Date from Job_Record jr"
        return SQL

def updateDateFormat(record, date):
    id = str(record)
    date = str(date)
    #SQL = "UPDATE Job_Record SET  Start_Date='" + date +"' WHERE Job_ID='" + id + "';"
    SQL = "UPDATE Job_Record SET  End_Date='" + date +"' WHERE Job_ID='" + id + "';"
    return SQL