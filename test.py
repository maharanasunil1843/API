from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/abc', methods = ['GET', 'POST'])
#GET and POST send data, GET send through a url, POST send through a body
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify((str(result)))

@app.route('/abc1/sunil', methods = ['GET', 'POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify((str(result)))

if __name__ == '__main__': #this invokes the entire python class
    app.run()


