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

Task:
1. Write a program to insert a record in sql table via api database
2. Write a program to update a record via api
3. Write a program to delete a record via api
4. Write a program to detch a record via api
5. All the abov questions you have to anser for mongo db as well.
