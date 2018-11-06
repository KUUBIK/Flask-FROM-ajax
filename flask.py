

from flask import Flask, render_template, session, request, json, jsonify
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/youdatabase"
mongo = PyMongo(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ap', methods=['GET', 'POST'])
def get_len():
    name = request.form['name'];
    return json.dumps({'len': '/static/car1.png'} )


@app.route('/as', methods=['GET', 'POST'])
def get_lep():
    name1 = request.form['name1'];
    return json.dumps({'lep': '/static/car2.png'} )

# @app.route('/')
# def add():
#     user = mongo.db.users
#     # user.insert([{"_id": 1 ,'car1':'/home/robert/androidflask/flaskled/tumblelog/photos/car1.png'},
#     #      {"_id": 2 ,'car2' : '/home/robert/androidflask/flaskled/tumblelog/photos/car2.png'},
#     #      {"_id": 3 ,'car3': '/home/robert/androidflask/flaskled/tumblelog/photos/car3.png'}])
#     # for men in user.find():
#     #     print (men)



if __name__ == '__main__':
    app.run(debug=True)


