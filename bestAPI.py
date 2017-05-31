# coding=utf-8
import json
from flask import Flask, request, url_for
app = Flask(__name__)

tasks =[
    {
        'id':1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route("/")
def hello():
    return "hello world"

@app.route('/query_user', methods = ['GET', 'POST'])
def query_user():  # 另一种传参数的方法，localhost:5000/query_user?id=123456
    id = request.args.get('id')
    jsonStr = json.dumps(tasks)
    return jsonStr

def check_json_format(raw_msg):
    if isinstance(raw_msg, str):       # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False

@app.route('/test_post', methods=['POST'])
def test_post():  # 另一种传参数的方法，localhost:5000/test_post
    data = request.get_data()
    if check_json_format(data):
        dict1 = json.loads(data)
        # jsonStr = json.dumps(tasks)
        print type(dict1), str(dict1).decode("unicode_escape")
        print dict1["body"]["data"][0]["baiduusername"]
    else:
        print data

@app.route("/index/<username>")
def index(username):
    return username

@app.route('/apiBaidu/queryData', methods=['POST'])
def queryData():
    data = request.get_data()

if __name__ == "__main__":
    app.run()
