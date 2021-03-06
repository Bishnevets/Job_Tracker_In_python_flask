
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
    SQL += "WHERE jr.Job_Status = 2 AND jr.End_Date  >= date('now','localtime', 'weekday 0', '-7 days');"
    return SQL


def SelectCompleteThisMonthCount():
    SQL = "SELECT Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr " 
    SQL += "WHERE jr.Job_Status = 2 AND jr.End_Date  >= date('now','localtime','start of month');"
    return SQL


def  SelectLastJobRecord():
    SQL = "SELECT Max(Job_ID) FROM Job_Record jr;"
    return SQL

def SelectFinalOperation(id):
    SQL = "SELECT Last_Operation from Job_Record jr Where Job_ID = '" + str(id) + "'"
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


def SelectStatusById(id):
    SQL = "SELECT status FROM Job_Status WHERE Status_ID = '" + str(id) + "'"
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


def SelectCompletedJobList(query_type):
    if query_type == 'all':
        SQL = "SELECT jr.Job_ID, jr.Job, jr.Work_Order, wc.Cell, js.Status, Job_Weight AS [Weight], "
        SQL += "MAX(a.Activity_ID) AS [Activity ID], o.First_Name || ' '|| o.Last_Name AS [Current Operator], "
        SQL += "jr.End_Date || ' ' || jr.End_Time AS [Completed On]"
        SQL += "FROM Job_Record jr JOIN Activity a on a.Job_Id = jr.Job_ID "
        SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
        SQL +=  "JOIN Job_Status js ON js.Status_ID = jr.Job_Status "
        SQL +=  "JOIN Operators o On a.Operator = o.Operator_ID " 
        SQL += "WHERE jr.Job_Status IN (2) "
        SQL += "GROUP BY a.Job_Id ORDER BY jr.End_Date DESC;"

    elif query_type == 'today':
        SQL = "SELECT jr.Job_ID, jr.Job, jr.Work_Order, wc.Cell, js.Status, Job_Weight AS [Weight], "
        SQL += "MAX(a.Activity_ID) AS [Activity ID], o.First_Name || ' '|| o.Last_Name AS [Current Operator], "
        SQL += "jr.End_Date || ' ' || jr.End_Time AS [Completed On]"
        SQL += "FROM Job_Record jr JOIN Activity a on a.Job_Id = jr.Job_ID "
        SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
        SQL +=  "JOIN Job_Status js ON js.Status_ID = jr.Job_Status "
        SQL +=  "JOIN Operators o On a.Operator = o.Operator_ID " 
        SQL += "WHERE jr.Job_Status IN (2) AND jr.End_Date  = DATE('now','localtime')"
        SQL += "GROUP BY a.Job_Id ORDER BY jr.End_Date DESC;"

    elif query_type == 'week':
        SQL = "SELECT jr.Job_ID, jr.Job, jr.Work_Order, wc.Cell, js.Status, Job_Weight AS [Weight], "
        SQL += "MAX(a.Activity_ID) AS [Activity ID], o.First_Name || ' '|| o.Last_Name AS [Current Operator], "
        SQL += "jr.End_Date || ' ' || jr.End_Time AS [Completed On]"
        SQL += "FROM Job_Record jr JOIN Activity a on a.Job_Id = jr.Job_ID "
        SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
        SQL +=  "JOIN Job_Status js ON js.Status_ID = jr.Job_Status "
        SQL +=  "JOIN Operators o On a.Operator = o.Operator_ID " 
        SQL += "WHERE jr.Job_Status IN (2) AND jr.End_Date  >= date('now','localtime', 'weekday 0', '-7 days')"
        SQL += "GROUP BY a.Job_Id ORDER BY jr.End_Date DESC;"

    elif query_type == 'month':
        SQL = "SELECT jr.Job_ID, jr.Job, jr.Work_Order, wc.Cell, js.Status, Job_Weight AS [Weight], "
        SQL += "MAX(a.Activity_ID) AS [Activity ID], o.First_Name || ' '|| o.Last_Name AS [Current Operator], "
        SQL += "jr.End_Date || ' ' || jr.End_Time AS [Completed On]"
        SQL += "FROM Job_Record jr JOIN Activity a on a.Job_Id = jr.Job_ID "
        SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
        SQL +=  "JOIN Job_Status js ON js.Status_ID = jr.Job_Status "
        SQL +=  "JOIN Operators o On a.Operator = o.Operator_ID " 
        SQL += "WHERE jr.Job_Status IN (2) AND jr.End_Date  >= date('now','localtime','start of month')"
        SQL += "GROUP BY a.Job_Id ORDER BY jr.End_Date DESC;"

    elif query_type == 'yesterday':
        SQL = "SELECT jr.Job_ID, jr.Job, jr.Work_Order, wc.Cell, js.Status, Job_Weight AS [Weight], "
        SQL += "MAX(a.Activity_ID) AS [Activity ID], o.First_Name || ' '|| o.Last_Name AS [Current Operator], "
        SQL += "jr.End_Date || ' ' || jr.End_Time AS [Completed On]"
        SQL += "FROM Job_Record jr JOIN Activity a on a.Job_Id = jr.Job_ID "
        SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
        SQL +=  "JOIN Job_Status js ON js.Status_ID = jr.Job_Status "
        SQL +=  "JOIN Operators o On a.Operator = o.Operator_ID " 
        SQL += "WHERE jr.Job_Status IN (2) AND jr.End_Date  = DATE('now','localtime','-1 days')"
        SQL += "GROUP BY a.Job_Id ORDER BY jr.End_Date DESC;"
    
    elif query_type.split(',')[0] == 'range':
        range_1 = query_type.split(',')[1]
        range_2 = query_type.split(',')[2]
        SQL = "SELECT jr.Job_ID, jr.Job, jr.Work_Order, wc.Cell, js.Status, Job_Weight AS [Weight], "
        SQL += "MAX(a.Activity_ID) AS [Activity ID], o.First_Name || ' '|| o.Last_Name AS [Current Operator], "
        SQL += "jr.End_Date || ' ' || jr.End_Time AS [Completed On]"
        SQL += "FROM Job_Record jr JOIN Activity a on a.Job_Id = jr.Job_ID "
        SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
        SQL +=  "JOIN Job_Status js ON js.Status_ID = jr.Job_Status "
        SQL +=  "JOIN Operators o On a.Operator = o.Operator_ID " 
        SQL += "WHERE jr.Job_Status IN (2)  AND jr.End_Date  >= '" + range_1 + "' AND jr.End_Date <= '" + range_2+ "' "
        SQL += "GROUP BY a.Job_Id ORDER BY jr.End_Date DESC;"
    else:
        SQL = "" 
    
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



def SelectCompleteByWorkCellDaily():
        SQL = "SELECT wc.Cell, Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr "
        SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
        SQL += "WHERE jr.Job_Status = 2 "
        SQL += "AND jr.End_Date  = DATE('now','localtime' ) "
        # SQL += "AND jr.End_Date  = '2021-01-26' "
        SQL += "group by jr.Work_Cell;"
        return SQL






def SelectNightlyReportQuerey():
    SQL =  "SELECT o.First_Name || ' '|| o.Last_Name AS [Name], "
    SQL += "jr.Job, jr.Work_Order, wc.Cell, jc.'Type' , js.Status, Job_Weight AS [Weight], "
    SQL += "MAX(a.Activity_ID) AS [Activity ID], a.Activity_Date ||' '|| a.Activity_Time AS [Last Activity], "
    SQL += "jr.Notes " 
    SQL += "FROM Job_Record jr JOIN Activity a on a.Job_Id = jr.Job_ID " 
    SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell "
    SQL += "JOIN Job_Status js ON js.Status_ID = jr.Job_Status "
    SQL += "JOIN Job_Categories jc on jc.Type_ID = jr.Job_Type "
    SQL += "JOIN Operators o On a.Operator = o.Operator_ID "
    SQL += "AND a.Activity_Date = DATE('now','localtime','-6 days') "
    SQL += "AND o.Shift = 2 "
    SQL += "GROUP BY a.Job_Id;"
    return SQL




def selectCountAggregates():
    SQL = "SELECT jr.End_Date, wc.Cell, Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr "
    SQL += "JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell " 
    SQL += "WHERE jr.Job_Status = 2 "
    SQL += "group by jr.End_Date, wc.Cell; "
    return SQL




def SelectJobTypeCount(routing):
    SQL = ""

    # Normal Day
    if routing == 0:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 1 "
        SQL += "AND Job_Status IN (1,2,3) "
        SQL += "AND JR.End_Date = DATE('now','localtime');"

    # rework Day
    if routing == 1:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 2 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date = DATE('now','localtime');"

    # DOE Day
    if routing == 2:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 3 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date = DATE('now','localtime');"


        
    # Normal week
    if routing == 3:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 1 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date >= date('now','localtime', 'weekday 0', '-7 days');"
    # rework week
    if routing == 4:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 2 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date >= date('now','localtime', 'weekday 0', '-7 days');"
    # DOE week
    if routing == 5:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 3 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date >= date('now','localtime', 'weekday 0', '-7 days');"
    
    
    
    # Normal Month
    if routing == 6:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 1 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date >= date('now','localtime','start of month');"
    # Rework Month
    if routing == 7:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 2 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date >= date('now','localtime','start of month');"
    # DOE Month
    if routing == 8:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 3 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date >= date('now','localtime','start of month');"
   
   
   
   
   # Normal Year
    if routing == 9:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 1 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date >= date('now','localtime','start of year');"
    # Rework Year
    if routing == 10:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 2 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date >= date('now','localtime','start of year');"
    # DOE Year
    if routing == 11:
        SQL = "SELECT count(Job_ID) " 
        SQL += "FROM Job_Record jr "
        SQL += "WHERE Job_Type = 3 "
        SQL += "AND Job_Status = 2 "
        SQL += "AND JR.End_Date >= date('now','localtime','start of year');"
    
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




def UpdateJobNotes(details):
    ID    = str(details['jobID'])
    notes = str(details['notes'])
    SQL = "UPDATE Job_Record "
    SQL += "SET Notes='" + notes + "' " 
    SQL += "WHERE Job_ID='" + ID + "';"
    return SQL





# -----------------------------------DELETE STATEMENTS-----------------------------------------------------------

#------------------------------------SPECIAL STATEMENTS----------------------------------------------------------

def selectDateToUpdate(query):

        if query == 1:
            SQL = "SELECT Job_ID, Start_Date from Job_Record jr"
        elif query == 2:
            SQL = "SELECT Job_ID, End_Date from Job_Record jr"
        elif query == 3:
            SQL = "SELECT Activity_ID, Activity_Date from Activity"
        return SQL

def updateDateFormat(record, date, query):
    
    id = str(record)
    date = str(date)

    if query == 1:
        SQL = "UPDATE Job_Record SET  Start_Date='" + date +"' WHERE Job_ID='" + id + "';"
    elif query == 2:
        SQL = "UPDATE Job_Record SET  End_Date='" + date +"' WHERE Job_ID='" + id + "';"
    elif query == 3:
        SQL = "UPDATE Activity SET Activity_Date='" + date + "' WHERE Activity_ID='" + id + "';" 
    return SQL












    
# SELECT jr.End_Date, COUNT(jr.Job_ID) AS [Large Hock] FROM Job_Record jr WHERE jr.Job_Status = 2 AND jr.Work_Cell = 1 Group by jr.End_Date ORDER BY jr.End_Date DESC;

# SELECT jr.End_Date, COUNT(jr.Job_ID) AS [Pilot Hock] FROM Job_Record jr WHERE jr.Job_Status = 2 AND jr.Work_Cell = 2 Group by jr.End_Date ORDER BY jr.End_Date DESC;

# SELECT jr.End_Date, COUNT(jr.Job_ID) AS [2 Gal Ross] FROM Job_Record jr WHERE jr.Job_Status = 2 AND jr.Work_Cell = 3 Group by jr.End_Date ORDER BY jr.End_Date DESC;

# SELECT jr.End_Date, COUNT(jr.Job_ID) AS [10 Gal Ross] FROM Job_Record jr WHERE jr.Job_Status = 2 AND jr.Work_Cell = 4 Group by jr.End_Date ORDER BY jr.End_Date DESC;

# SELECT jr.End_Date, COUNT(jr.Job_ID) AS [40 Gal Ross] FROM Job_Record jr WHERE jr.Job_Status = 2 AND jr.Work_Cell = 5 Group by jr.End_Date ORDER BY jr.End_Date DESC;

# SELECT jr.End_Date, COUNT(jr.Job_ID) AS [100 Gal Ross] FROM Job_Record jr WHERE jr.Job_Status = 2 AND jr.Work_Cell = 6 Group by jr.End_Date ORDER BY jr.End_Date DESC;

# SELECT jr.End_Date, COUNT(jr.Job_ID) AS [Mezz Tank] FROM Job_Record jr WHERE jr.Job_Status = 2 AND jr.Work_Cell = 7 Group by jr.End_Date ORDER BY jr.End_Date DESC;

# SELECT jr.End_Date, COUNT(jr.Job_ID) AS [Activator] FROM Job_Record jr WHERE jr.Job_Status = 2 AND jr.Work_Cell = 8 Group by jr.End_Date ORDER BY jr.End_Date DESC;

# SELECT jr.End_Date, COUNT(jr.Job_ID) AS [1/2 Gal Ross] FROM Job_Record jr WHERE jr.Job_Status = 2 AND jr.Work_Cell = 7 Group by jr.End_Date ORDER BY jr.End_Date DESC;
