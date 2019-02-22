from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from pprint import pprint
from bson.json_util import dumps
from flask import abort
import json

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'magic'
app.config['MONGO_URI'] = "mongodb://msm98:paras123@cluster0-shard-00-00-4gnmc.mongodb.net:27017,cluster0-shard-00-01-4gnmc.mongodb.net:27017,cluster0-shard-00-02-4gnmc.mongodb.net:27017/magic?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
mongo = PyMongo(app)
collect = mongo.db['test101']

@app.route('/', methods=['PUT'])
def get_all_frameworks():
	if request.data is None or request.data == '':
		abort(404)
	post = json.loads(request.data)
	post_id = collect.insert_one(post).inserted_id
	if(post_id):
		return jsonify({'ok':True,'message':'User Created Successfully'}),200
	else:
		return jsonify({'ok':False,'message':'Bad request'}),400

@app.route('/',methods=['GET'])
def find_by_details():
	if request.args.get('id') is not None:
		query = collect.find({"id": request.args.get('id')})
	elif request.args.get('name') is not None:
		query = collect.find({"name": {'$regex' : request.args.get('name'), '$options' : 'i'}})
	else:
		query = collect.find()
	if query.count() != 0:
		return dumps(query)
	else:
		abort(404)

@app.route('/',methods=['DELETE'])
def delete_many_by_id():
	user = request.args.get('id')
	return str(collect.delete_many({"id": user}).deleted_count) + " documents deleted."
	
if __name__=='__main__':
	app.run(debug=True)


# client = MongoClient("mongodb://msm98:paras123@cluster0-shard-00-00-4gnmc.mongodb.net:27017,cluster0-shard-00-01-4gnmc.mongodb.net:27017,cluster0-shard-00-02-4gnmc.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
# db = client.magic
# collection = db['test101']

