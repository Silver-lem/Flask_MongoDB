from flask import Flask,request
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

@app.route('/submit',methods=['POST'])
def submit():
    # name = request.form.get('name')
    # return 'Hello, ' + name + '!'
    form_data = dict(request.form)

    # print(form_data)
    collection.insert_one(form_data)

    # return form_data
    return "data submitted succesfully"

@app.route('/view')
def view():

    data = collection.find()
    data = list(data)
    # print(data) -- A cursor is a list of objects a collect is a list of json objects
    for item in data:
        print(item)

        del item['_id']

    data = {
        'data' : data
    }

    # return "data retrieved succesfully"
    return data

if __name__ == '__main__':
    app.run(debug=True)