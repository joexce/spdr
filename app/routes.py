from app import app
from flask import Flask, request, json, Response
from pymongo import MongoClient
import logging as log

class dbConnector:
    def __init__(self):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        self.client = MongoClient("mongodb://localhost:27017/")

        cursor = self.client['spdr']
        self.collection = cursor['status']

    def getStatus(self):
        documents = self.collection.find()
        result = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return result
    
    def createStatus(self, data):
        response = self.collection.insert_one(data)
        result = {'Status': 'Successfully Inserted','Document_ID': str(response.inserted_id)}
        return result

@app.route('/status', methods=['GET'])
def getStatus():
    res = dbConnector().getStatus()
    return Response(response=json.dumps(res),status=200,mimetype='application/json')

@app.route('/status', methods=['POST'])
def createStatus():
    req = request.json
    res = dbConnector().createStatus(req)
    return Response(response=json.dumps(res),status=200,mimetype='application/json')