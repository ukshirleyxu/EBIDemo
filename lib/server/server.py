from flask import Flask, request, jsonify
from pymongo import MongoClient
import pprint
import pysolr

app = Flask(__name__)


client = MongoClient('localhost', 27017);
dblist=client.database_names();
db = client.bio
Documents = db.documents;

solr = pysolr.Solr('http://localhost:8983/solr/bio/', timeout=10)





#pprint.pprint(resutls)
#@app.route('/api/creat')
#request.args.get('queryName'); return none if it does not exist.
#request.form.get('paramsName');
#req_data=request.get_json()

@app.route('/api/insert',methods=['POST'])
def hello_world():
	req_data=request.get_json()
	pprint.pprint(req_data)
	Documents.insert_one(req_data)
	res = list(Documents.find());
	data = []
	for item in res:
		obj = {
			'name':item['data']
		}
		data.append(obj)
	return jsonify(res=data), 200;

@app.route('/api/searchmongo')
def searchmongo():
	data=[]
	req_data = request.args.get('data');
	pprint.pprint(req_data);
	res = list(Documents.find({"data": req_data})) 
	for item in res:
		pprint.pprint(item)
		obj = {
			'name':item['data']
		}
		data.append(obj)
		pprint.pprint(data)
	#response = jsonify(data)
	#response.status_code = 200
	#return response;
	return jsonify(res=data), 200;

@app.route('/api/searchsolr')
def searchsolr():
	data=[]
	req_data = request.args.get('age');
	res = solr.search('age:[* TO  '+req_data+']');
	for item in res:
		pprint.pprint(item)
		obj = {
			'name':item['data'],
			'age':item['age']
		}
		data.append(obj)
		pprint.pprint(data)
	#response = jsonify(data)
	#response.status_code = 200
	#return response;
	return jsonify(res=data), 200;

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True, threaded=True, processes=3)