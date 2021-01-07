from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
import os
import csv



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


@app.route("/names")
def names():
    # read from file to display
    path = "names.csv"
    with open(path,'r') as file:
        reader = csv.reader(file)
        nameList = list(reader)

    return render_template('/names.html',nameList=nameList)



@app.route("/form/", methods=['POST','GET'])
def form():
    # write to file from form when posted
    if request.method == 'POST':

        errors = False

        if not request.form['first_name']:
            errors = True

        if not request.form['last_name']:
            errors = True

        
        if not errors:

           
            first_name = request.form['first_name']
            last_name = request.form['last_name']

            path = "names.csv"
            file = open(path,'a')
            writer = csv.writer(file)
            writer.writerow((first_name,last_name))
            file.close

            fullname = first_name + " " + last_name


            return redirect('/names')



        else:
            return render_template('form.html')
        
    else:
        return render_template('form.html')








if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=5000)
