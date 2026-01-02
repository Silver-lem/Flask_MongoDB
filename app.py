from flask import Flask,request,render_template
from datetime import datetime

app = Flask(__name__) #An instance of flask class

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    # print(day_of_week)
    return render_template('index.html',day_of_the_week=day_of_week,current_time=current_time)


@app.route('/time')
def time():
    current_time = datetime.now().strftime('%H:%M:%S')
    return current_time


@app.route('/submit',methods=['POST'])
def submit():
    name = request.form.get('name')

    return 'Hello, ' + name + '!'

if __name__ == '__main__':
    app.run(debug=True)