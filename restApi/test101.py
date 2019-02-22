from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from pprint import pprint
from bson.json_util import dumps
from bson import json_util
import datetime
import json

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'magic'
app.config['MONGO_URI'] = "mongodb://msm98:paras123@cluster0-shard-00-00-4gnmc.mongodb.net:27017,cluster0-shard-00-01-4gnmc.mongodb.net:27017,cluster0-shard-00-02-4gnmc.mongodb.net:27017/magic?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
mongo = PyMongo(app)
collect = mongo.db['test101']

@app.route('/add', methods=['GET'])
def get_all_frameworks():
	post = {"name": "Mike",
	"id": "123",
	"language": "python",
	"framework": "framework"
	}
	post_id = collect.insert_one(post).inserted_id
	if(post_id):
		return jsonify({'ok':True,'message':'User Created Successfully'}),200
	else:
		return jsonify({'ok':False,'message':'Bad request'}),400
# output = []

# for q in framework.find():
#     output.append({'name' : q['name'], 'language' : q['language']})

# return jsonify({'result' : output})

@app.route('/data/<string:user_id>',methods=['GET'])
def find_by_id(user_id):
	output = []
	cur = list(collect.find({}))
	for i in json.dumps( cur , indent=4, default=json_util.default).split(","):
		output.append(i)
	return jsonify({'result':output})
if __name__=='__main__':
	app.run(debug=True)


# client = MongoClient("mongodb://msm98:paras123@cluster0-shard-00-00-4gnmc.mongodb.net:27017,cluster0-shard-00-01-4gnmc.mongodb.net:27017,cluster0-shard-00-02-4gnmc.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
# db = client.magic
# collection = db['test101']

