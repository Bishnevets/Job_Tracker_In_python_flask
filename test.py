from data import DB, util
from datetime import datetime
from flask import json, jsonify


now = datetime.now()
time = now.strftime('%I:%M %p')
date = now.strftime('%m-%d-%Y')

# date = (now.strftime('%A %B %d, %Y'))

operationValues = [10,20,30,40,50]


for v in operationValues:
    print(v)


