from flask import Flask
from flask import render_template
from flask import request
#from flask import redirect, url_for
import os
from os import listdir

app = Flask(__name__)

#http://127.0.0.1:5000
@app.route('/')
def main_page():
    return render_template('task.html')

#http://127.0.0.1:5000/Purchase
@app.route("/Purchase",methods = ['GET'])
def purchase():
    return render_template('purchase.html')


#http://127.0.0.1:5000/Sale
@app.route("/Sale", methods = ['GET'])
def sale():
    return render_template('sale.html')

#http://127.0.0.1:5000/Balance
@app.route("/Balance", methods = ['GET'])
def balance():
    return render_template('balance.html')

#http://127.0.0.1:5000/List-History
@app.route("/List-History", methods = ['GET'])
def history():
    log = request.form.get('from', 'to')
    if request.method == 'GET' and log:
        print(listdir)
    #write to a file
    path = os.path.join(os.getcwd(), "log.txt")
    with open(path, 'w') as fp:
        fp.write((str(f"Log: {log}")))
    return render_template('history.html')