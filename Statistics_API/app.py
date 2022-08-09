from flask import Flask
from logging import Logger
from KSTest import KS_Test
import array as arr
from flask import request
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
    return ("Post readings to /test to run KS test")
@app.route('/kstest', methods = ['POST'])
def KSTest():
    readings = request.form['readings']
    test = KS_Test();
    data = readings.split(',')
    input = readings1 =[int(g)for g in data]
    result = test.run(input);
    jsonresult = json.dumps(result)
    return (jsonresult)

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)