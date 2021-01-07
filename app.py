from flask import Flask, render_template, request, redirect
from markupsafe import escape
import os
import csv
from data import DB



# web application instance
app = Flask(__name__)


#database setup using sqlalchemy --change the database name accordingly
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#db = SQLAlchemy(app)


#-------------------------Alchemy Models--------------------------------------- 


#-------------------------lists and veriables--------------------------------------- 





#-------------------------routing--------------------------------------- 

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')



@app.route("/new_job/", methods=['POST','GET'])
def form():
    oplist = DB.getActiveOperators()
    typeList = DB.getJobType()
    workcellList = DB.getWorkCells()
    return render_template('new_job.html', oplist=oplist,typeList=typeList,workcellList=workcellList)




if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=5000)
