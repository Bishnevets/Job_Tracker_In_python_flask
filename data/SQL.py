
# -----------------------------------SELECT SATEMENTS-----------------------------------------------------------


def SelectRunningJobsCount():
    SQL = "SELECT Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr WHERE jr.Job_Status  in (1,3,4,7)"
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





# -----------------------------------INSERT SATEMENTS-----------------------------------------------------------


def InsertIntoJobRecord(newRecord):

    job   = newRecord['job']
    WO    = newRecord['workOrder']
    weig  = newRecord['jobWeight']
    cell  = newRecord['workCell']
    jtype = newRecord['jobType']
    stat  = newRecord['jobStatus']
    time  = newRecord['startTime']
    note  = newRecord['notes']
    test  = newRecord['inProcessTesting']
    PA    = newRecord['preAdjustments']
    tops  = newRecord['totalOperatiions']
    date  = newRecord['startDate']
    last  = newRecord['lastOperation']

    SQL = "INSERT INTO Job_Record (Job, Work_Order, Job_Weight, Work_Cell, Job_Type, Job_Status, "
    SQL += "Start_Time, Notes, 'In-Process_Testing', Pre_Adjustment, Total_Operations, Start_Date, Last_Operation) "
    SQL += "VALUES( " 
    SQL += job + ", " + WO + ", " + weig + ", " + cell + ", " + jtype + ", " + stat + ", " + note + ", " 
    SQL += time + ", " + PA + ", " + tops + ", " + date + ", " + last + ");"
    return SQL



def InsertIntoActivity(newRecord,JobIndex):

    oper  = newRecord['operator']
    acti  = newRecord['Activity']
    date  = newRecord['startDate']
    last  = newRecord['lastOperation']
    time  = newRecord['startTime']
    
    SQL = "INSERT INTO Activity(Operator, Activity, Activity_Date, Job_Id, Operation, Activity_Time) "
    SQL += "VALUES( " 
    SQL += oper + ", " + acti + ", " + date + ", " + JobIndex + ", " + last + ", " + time +");"
    return SQL


# -----------------------------------UPDATE SATEMENTS-----------------------------------------------------------


# -----------------------------------DELETE SATEMENTS-----------------------------------------------------------