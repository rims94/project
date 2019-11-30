from flask import Flask,render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/index')
def index():
    now = datetime.now()
    timeString = now.strftime("%d/%m/%Y %H:%M")
    templateData ={
        'title':'Hello',
        'time':timeString
        }
    return render_template('index500.html', **templateData)

if (__name__) == '(__main__)' :
    app.run(debug = True)

