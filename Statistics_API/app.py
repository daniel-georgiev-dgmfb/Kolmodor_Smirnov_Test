from flask import Flask
from logging import Logger
from KSTest import KS_Test
from RunningStats import RunningStats
import array as arr
from flask import request
from scipy import stats
from ModeResult import ModeResult
import numpy as np
import json
# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/home', methods = ['GET'])
def home():
    return ("Post readings to /specificFunction to get a result")

@app.route('/stats/tests/kstest', methods = ['POST'])
def KSTest():
    readings = request.form;
    data = readings['readings'];
    test = KS_Test();
    data = data.split(',')
    input = readings1 =[int(g)for g in data]
    result = test.run(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/skew', methods = ['POST'])
def skew():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = readings1 =[int(g)for g in data]
    #runningStats = RunningStats();
    #r = runningStats.skew(input);
    result = stats.skew(input)
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/kurtosis', methods = ['POST'])
def kurtosis():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = readings1 =[int(g)for g in data]
    #runningStats = RunningStats();
    result = stats.kurtosis(input)
    #result1 = runningStats.kurtosis(input)
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/variance', methods = ['POST'])
def trimedvariance():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = readings1 =[int(g)for g in data]
    result = stats.tvar(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/sdeviation', methods = ['POST'])
def standarddeviation():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = [int(g)for g in data]
    result = stats.tstd(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/mode', methods = ['POST'])
def mode():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input =[int(g)for g in data]
    result = stats.mode(input, axis=None)
    mode = result.mode;
    count = result.count;
    try:
        dic = dict();
        for i in [0,0]:
            key = str(mode[i])
            dic[key] = str(count[i]);
        jsonres = json.dumps(dic);
        return jsonres
    except:
        raise;

@app.route('/stats/funcs/standarderror', methods = ['POST'])
def standarderror():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = readings1 =[int(g)for g in data]
    #runningStats = RunningStats();
    result = stats.sem(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)