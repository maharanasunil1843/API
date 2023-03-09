from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://maharanasunil1843:Sunil131096@cluster0.tmhnkhm.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database1 = client['taskdb']
collection = database1['taskcollection']

@app.route("/insert/mongo", methods = ["POST"])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str("successfully inserted"))
if __name__ =='__main__':
    app.run(port=5001)