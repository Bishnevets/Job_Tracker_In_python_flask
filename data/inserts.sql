INSERT INTO Job_Record (
	Job, 
	Work_Order, 
	Job_Weight, 
	Work_Cell, 
	Job_Type, 
	Job_Status, 
	Start_Time, 
	Notes, 
	"In-Process_Testing", 
	Pre_Adjustment, 
	End_Time, 
	Total_Operations, 
	Start_Date, 
	End_Date, 
	Last_Operation)
VALUES('X-999-99-9', '123456', 100, 3, 1, 1, 'start time', 'Notes', 0, 0, 'End time', 1, 'start date', 'end date', 20);






SELECT * FROM Job_Record jr 
WHERE Job = 'X-999-99-9'




INSERT INTO Activity(
	Operator, 
	Activity, 
	Activity_Date, 
	Job_Id, 
	Operation, 
	Activity_Time)
VALUES(12, 4, 'date', 689, 20, 'Time');

SELECT * from Activity a