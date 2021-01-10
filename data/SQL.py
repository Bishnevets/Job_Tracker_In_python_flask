
# -----------------------------------SELECT SATEMENTS-----------------------------------------------------------


def SelectRunningJobsCount():
    SQL = "SELECT Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr WHERE jr.Job_Status  in (1,3,4,7)"
    return SQL


def SelectCompleteTodayCount():
    SQL = "SELECT Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr " 
    SQL += "WHERE jr.Job_Status = 2 AND jr.End_Date  = DATE('now');"
    return SQL


def SelectCompleteThisWeekCount():
    SQL = "SELECT Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr " 
    SQL += "WHERE jr.Job_Status = 2 AND jr.End_Date  >= date('now', 'weekday 1', '-7 days');"
    return SQL


def SelectCompleteThisMonthCount():
    SQL = "SELECT Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr " 
    SQL += "WHERE jr.Job_Status = 2 AND jr.End_Date  >= date('now','start of month');"
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



def SelectActiveOperators():
    SQL = "SELECT o.Operator_ID, o.First_Name || ' ' || o.Last_Name AS [Name], ds.Shift, os.Status "
    SQL += "FROM Operators o "
    SQL += "JOIN Dept_Shifts ds ON ds.Shift_ID = o.Shift "
    SQL += "JOIN Operator_Status os ON os.Status_ID = o.Status "
    SQL += "WHERE os.Status NOT IN ('Inactive') "
    SQL += "ORDER BY ds.Shift, [Name]"
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
    SQL += job + "', '" + WO + "', '" + weig + "', '" + cell + "', '" + jtype + "', '" + stat + "', '" + note + "', '" 
    SQL += time + "', '" + test + "', '" + PA + "', '" + tops + "', '" + date + "', '" + last + "');"
    return SQL



def InsertIntoActivity(newRecord,JobIndex):

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


# -----------------------------------UPDATE STATEMENTS-----------------------------------------------------------


# -----------------------------------DELETE STATEMENTS-----------------------------------------------------------