#Passing data in an unsecured manner to the browser

from flask import Flask, request, jsonify
app = Flask(__name__)

import mysql.connector as conn

@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get("mail_id")
    return "this is my first function for get {} {} {}".format(get_name, mobile_number, mail_id)

@app.route("/get_data")
def get_data():
    db = request.args.get("db")
    tn = request.args.get("tn")
    try:
        mydb = conn.connect(host="localhost", user="root", passwd="Sunil131096@", database=db)
        cursor = mydb.cursor()
        cursor.execute("select * from {}".format(tn))
        data = cursor.fetchall()
        mydb.commit()
        mydb.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__ == "__main__":
    app.run(port = 5002)