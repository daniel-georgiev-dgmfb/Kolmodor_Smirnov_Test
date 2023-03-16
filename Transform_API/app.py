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

@app.route('/stats/funcs/fft', methods = ['POST'])
def FourierTransforms():
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

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)