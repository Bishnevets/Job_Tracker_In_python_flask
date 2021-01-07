from flask_sqlalchemy import SQLAlchemy
import sqlite3
import csv

def make_connection():
    connection_String = "C:\\Users\\sbish\\Desktop\\project x\\data\\JT_DATA.db"
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

