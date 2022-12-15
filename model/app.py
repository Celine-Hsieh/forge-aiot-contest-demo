# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2019 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import collections
import click
from flask import Flask, request
import json, requests 

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient()
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.sensor
collection = db.data2


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, hello!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'

sensor_list = ['temp', 'CO2', 'RH', 'PM25', 'PplCnt', 'OccStat', 'LgtStat', 'PNO', 'Ppl']

@app.route("/get_many_sensor", methods=["GET"])
def get_many_sensor():
    a = []
    numbers = request.args.get('num')
    for i in range(-int(numbers),0):
        senosr_dict = {}
        for sensor in sensor_list:
            b = []
            for x in db.data2.find({"sensor":sensor}):
                b.append(x["value"])
            # print(sensor)
            # print(b[-1])
            senosr_dict[sensor] = b[i]
        b = []
        for x in collection.find({"sensor":"Temp"}):
            b.append(x["date"])
        # print(b[-1])
        senosr_dict["time"] = b[i]
        c = json.dumps(senosr_dict)
        a.append(c)
    return str(json.dumps(a))
    # return numbers

@app.route('/sensor_now')
def now_sensor():
    senosr_dict = dict()
    for sensor in sensor_list:
        b = []
        for x in db.data2.find({"sensor":sensor}):
            b.append(x["value"])
        senosr_dict[sensor] = b[-1]
    b = []
    for x in collection.find({"sensor":"Temp"}):
        b.append(x["date"])
    # print(b[-1])
    senosr_dict["time"] = b[-1]
    return str(json.dumps(senosr_dict))

@app.route('/sensors')
def get_sensors():
    a = []
    for x in collection.find():
        x['_id'] = str(x['_id'])
        x = json.dumps(x)
        a.append(x)
    return str(a)

@app.route('/sensor/<name>')
def get_sensor_one(name):
    a = []
    for x in collection.find({"sensor":name}):
        x['_id'] = str(x['_id'])
        x = json.dumps(x)
        a.append(x)
    return str(a)

@app.route('/value/<name>')
def get_value(name):
    a = []
    for x in collection.find({"sensor":name}):
        a.append(x["value"])
    return str(a[-1])

@app.route('/value_all/<name>')
def get_value_all(name):
    a = []
    for x in collection.find({"sensor":name}):
        a.append(x["value"])
    return str(a)

###############################
@app.route('/temp_sensor')
def get_temp_sensor():
    a = []
    json_data = json.dumps({})
    for x in db.data2.find({"sensor":"Temp"}):
        x['_id'] = str(x['_id'])
        x = json.dumps(x)
        a.append(x)
    return str(a)


###############################################################################
@app.route('/temp')
def get_temp():
    a = []
    for x in collection.find({"sensor":"Temp"}):
        a.append(x["value"])
    return str(a[-1])
    
@app.route('/temp_all')
def get_temp_all():
    a = []
    for x in collection.find({"sensor":"Temp"}):
        a.append(x["value"])
    return str(a)

@app.route('/CO2')
def get_CO2():
    a = []
    for x in collection.find({"sensor":"CO2"}):
        a.append(x["value"])
    return str(a[-1])
    
@app.route('/CO2_all')
def get_CO2_all():
    a = []
    for x in collection.find({"sensor":"CO2"}):
        a.append(x["value"])
    return str(a)
    
#########
@app.route('/LgtStat')
def get_Lgt():
    a = []
    for x in collection.find({"sensor":"LgtStat"}):
        a.append(x["value"])
    return str(a[-1])
    
@app.route('/LgtStat_all')
def get_Lgt_all():
    a = []
    for x in collection.find({"sensor":"LgtStat"}):
        a.append(x["value"])
    return str(a)

###

@app.route('/RH')
def get_RH():
    a = []
    for x in collection.find({"sensor":"RH"}):
        a.append(x["value"])
    return str(a[-1])
    
@app.route('/RH_all')
def get_RH_all():
    a = []
    for x in collection.find({"sensor":"RH"}):
        a.append(x["value"])
    return str(a)

######

@app.route('/PNO')
def get_PNO():
    a = []
    for x in collection.find({"sensor":"PNO"}):
        a.append(x["value"])
    return str(a[-1])
    
@app.route('/PNO_all')
def get_PNO_all():
    a = []
    for x in collection.find({"sensor":"PNO"}):
        a.append(x["value"])
    return str(a)

######

@app.route('/OccStat')
def get_OccStat():
    a = []
    for x in collection.find({"sensor":"OccStat"}):
        a.append(x["value"])
    return str(a[-1])
    
@app.route('/OccStat_all')
def get_OccStat_all():
    a = []
    for x in collection.find({"sensor":"OccStat"}):
        a.append(x["value"])
    return str(a)

######

@app.route('/time')
def get_time():
    b = []
    for x in collection.find({"sensor":"Temp"}):
        b.append(x["date"])
    return b[-1]

@app.route('/time_all')
def get_time_all():
    b = []
    for x in collection.find({"sensor":"Temp"}):
        b.append(x["date"])
    return str(b)

#####

@app.route('/PM25')
def get_PM25():
    b = []
    for x in collection.find({"sensor":"PM25"}):
        b.append(x["date"])
    return b[-1]

@app.route('/PM25_all')
def get_PM25_all():
    b = []
    for x in collection.find({"sensor":"PM25"}):
        b.append(x["date"])
    return str(b)

#####

@app.route('/Ppl')
def get_Ppl():
    b = []
    for x in collection.find({"sensor":"Ppl"}):
        b.append(x["value"])
    # return str(b[-1])
    return str(json.dumps(b[-1]))

# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=4000)