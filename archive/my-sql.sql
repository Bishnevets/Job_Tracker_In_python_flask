
--Activity VIEW
SELECT 
	o.First_Name || ' '|| o.Last_Name AS [Name],
	jr.Job, 
	jr.Work_Order, 
	wc.Cell,
	js.Status, 
	a.Activity_Time AS "Time",
	a.Activity_Date AS "Date",
	a.Activity_ID,
	a.Operation,
	jr.Notes 
FROM Job_Record jr JOIN Activity a on a.Job_Id = jr.Job_ID
JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell
JOIN Job_Status js ON js.Status_ID = jr.Job_Status
JOIN Job_Categories jc  on jc.Type_ID = jr.Job_Type 
JOIN Operators o On a.Operator = o.Operator_ID
GROUP BY a.Job_Id;



--ME adjustements
SELECT 
	jr.Job, 
	jr.Work_Order,
	jr.Pre_Adjustment,
	jr."In-Process_Testing" 
FROM Job_Record jr 



SELECT 
	jr.Job_ID, 
	jr.Job, 
	jr.Work_Order, 
	wc.Cell,
	jc."Type" ,
	js.Status, 
	Job_Weight AS [Weight],
    MAX(a.Activity_ID) AS [Activity ID], 
    o.First_Name || ' '|| o.Last_Name AS [Current Operator],
    jr.Start_Date,
	jr.Start_Time,
    jr.End_Date,
    jr.End_Time
FROM Job_Record jr 
JOIN Activity a on a.Job_Id = jr.Job_ID
JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell
JOIN Job_Status js ON js.Status_ID = jr.Job_Status
JOIN Job_Categories jc  on jc.Type_ID = jr.Job_Type
JOIN Operators o On a.Operator = o.Operator_ID
WHERE jr.Job_Status IN (2)
GROUP BY a.Job_Id ORDER BY jr.End_Date DESC;


SELECT * from Work_Cells wc 






SELECT jr.End_Date, wc.Cell, Count(Job_ID ) AS [Jobs complete today] FROM Job_Record jr
JOIN Work_Cells wc ON wc.Cell_ID = jr.Work_Cell
WHERE jr.Job_Status = 2
group by jr.End_Date, wc.Cell;






