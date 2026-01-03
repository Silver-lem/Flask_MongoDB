from flask import Flask,request,render_template
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
uri = MONGO_URI

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test
collection = db['flask_test']

##############################################################################################

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
    # name = request.form.get('name')
    # return 'Hello, ' + name + '!'
    form_data = dict(request.form)

    print(form_data)
    return form_data

if __name__ == '__main__':
    app.run(debug=True)