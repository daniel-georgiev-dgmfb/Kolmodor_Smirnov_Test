from pickle import TUPLE
from flask import Flask
from logging import Logger
from KSTest import KS_Test
from RunningStats import RunningStats
#from scipy.spatial.distance import cdist
from scipy.spatial import distance
import array as arr
from flask import request
from scipy import stats
import numpy as np
#from ModeResult import ModeResult
import numpy as np
from scipy.stats import entropy
#from scipy import function_base
import json
from Cryptography import Hash
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

@app.route('/cryptography/funcs/hash', methods = ['POST'])
def hash():
    readings = request.form;
    data = readings['data'];
    hashAlg = readings['hashAlg'];
    h = Hash()
    hashed = h.generate(data, hashAlg)
    return (hashed)

@app.route('/stats/funcs/integrate', methods = ['POST'])
def integrate():
    readings = request.form;

    ydatareadings = readings['readingsy'];
    ydata = ydatareadings.split(',')
    yinput =[float(g.strip('[').strip(']')) for g in ydata]

    xdatareadings = readings['readingsx'];
    xdata = xdatareadings.split(',')
    xinput =[float(g.strip('[').strip(']')) for g in xdata]

    dx = readings['dx'];
    dx =float(dx)
    
    result = np.trapz(yinput, xinput,dx)
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/median', methods = ['POST'])
def median():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = [float(g)for g in data]
    result = np.median(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/mean', methods = ['POST'])
def mean():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = [float(g)for g in data]
    result = np.mean(input, 0, 'float');
    jsonresult = json.dumps(result)
    print(jsonresult)
    return (jsonresult)

@app.route('/stats/funcs/geometricmean', methods = ['POST'])
def geometricmean():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = [float(g)for g in data]
    result = stats.gmean(input, 0, 'float');
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/harmonicmean', methods = ['POST'])
def harmonicmean():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = [float(g)for g in data]
    result = stats.hmean(input, 0, 'float');
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/spatial/euclideandistance', methods = ['POST'])
def EuDistance():
    raise Exception("data type issue caused by user agent to be solve. Fiddler for instance")
    user_agent = request.user_agent.string;
    if user_agent == 'Fiddler':
        readings = request.data;
        readings1 = readings.split(',')
    else:
        readings = request.form;
        datax = readings['readingsx'];
        datay = readings['readingsy'];
    splitx = datax.split(',')
    splity = datay.split(',')
    datax = []
    datay = []
    
    for s in splitx:
        s1 = s.strip('[').strip(',]').split(',')
        d = [float(g)for g in s1];
        datax.append(d)

    for s in splity:
        s1 = s.strip('[').strip(',]').split(',')
        d = [float(g)for g in s1];
        datainty.append(d)

    result = distance.euclidean(datax, datay)
    jsonresult = json.dumps(result);
    return (jsonresult)

@app.route('/stats/tests/kstest', methods = ['POST'])
def KSTest():
    readings = request.form;
    data = readings['readings'];
    test = KS_Test();
    data = data.split(',')
    input = readings1 =[float(g)for g in data]
    result = test.run(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/skew', methods = ['POST'])
def skew():
    formReadings = request.form;
    #readings = request.data;
    data = formReadings['readings'];
    data = data.split(',')
    #data =[int(g) for g in data]
    #data = readings[0];
    #data = data.split(',')
    input = [float(g)for g in data]
    result = stats.skew(input)
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/kurtosis', methods = ['POST'])
def kurtosis():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = readings1 =[float(g)for g in data]
    result = stats.kurtosis(input)
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/variance', methods = ['POST'])
def trimedvariance():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = readings1 =[float(g)for g in data]
    result = stats.tvar(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/covariance', methods = ['POST'])
def covariance():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = readings1 =[float(g)for g in data]
    result = np.cov(input);
    r = result.max(), result.min()
    jsonresult = json.dumps(r);
    return (jsonresult)

@app.route('/stats/funcs/pearsoncoefficient', methods = ['POST'])
def pearson():
    readings = request.form;
    datax = readings['readingsx'];
    datax = datax.split(',')
    input = readings1 =[float(g) for g in datax]
    datay = readings['readingsy'];
    datay = datay.split(',')
    input1 = readings2 =[float(g) for g in datay]
    result = stats.pearsonr(input, input1)
    jsonresult = json.dumps(tuple({ result[0], result[1] }))
    return (jsonresult)

@app.route('/stats/funcs/sdeviation', methods = ['POST'])
def standarddeviation():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = [float(g)for g in data]
    result = stats.tstd(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/entropy', methods = ['POST'])
def entropy():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = [float(g)for g in data]
    result = stats.entropy(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/funcs/mode', methods = ['POST'])
def mode():
    readings = request.form;
    data = readings['readings'];
    axis = readings['axis']
    data = data.split(',')
    input =[float(g)for g in data]
    if axis == 'None':
        axisInt = 0
    else:
        axisInt = int(axis);
    result = stats.mode(input, axisInt)
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
    input = readings1 =[float(g)for g in data]
    result = stats.sem(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

@app.route('/stats/tests/ttest', methods = ['POST'])
def TTest():
    readings = request.form;
    data = readings['readings'];
    data = data.split(',')
    input = [float(g)for g in data]
    result = stats.ttest_1samp(input, 0.00);
    jsonresult = json.dumps(result)
    return (jsonresult)

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)