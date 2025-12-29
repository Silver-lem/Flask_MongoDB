from flask import Flask,request

app = Flask(__name__) #An instance of flask class

@app.route('/')
def home():
    return "<h1>Hello World</h1>"

@app.route('/<name>')
def second(name):
    return "Hello " + name

@app.route('/<a>/<b>')
def third(a,b):
    sum = int(a) + int(b) #using int() to typecast since by default it is considered to be a string

    result = {
        'ans' : sum
    }

    # return str(result)
    return result

@app.route('/api')
def func():
    name = request.values.get('name')
    age = request.values.get('age')

    result = {
        'name' : name,
        'age' : age
    }

    return result

if __name__ == '__main__':
    app.run(debug=True)


