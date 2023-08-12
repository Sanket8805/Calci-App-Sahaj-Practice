from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    n1= data["first"]
    n2=data["second"]
    sum_add=n1+n2
    return { "result": sum_add }

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    n1 = data["first"]
    n2 = data["second"]
    sub1=n1-n2
    return { "result": sub1}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')