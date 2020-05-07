import pymongo
from pymongo import MongoClient
import urllib
from bson.objectid import ObjectId

class MongoDBUtility:
    def __init__(self, url, database, collection_name):
        try:
            mongo_url = url
            cluster = MongoClient(mongo_url)
            db = cluster[database]
            self.collection = db[collection_name]
        except Exception as exp:
            print("Error occurred while connecting to database " + str(exp))

    def execute_query(self, query, query_type):
        try:
            if query_type.lower() == "select":
                if len(query) == 2:
                    result = self.collection.find(query[0], query[1])
                else:
                    result = self.collection.find(query[0])

                return {"status": "SUCCESS", "result": result}

            elif query_type.lower() == "insert":
                self.collection.insert_one(query)

                return {"status": "SUCCESS", "result": "insert operation was successful"}

            elif query_type.lower() == "delete":
                self.collection.delete_one({"_id": ObjectId(query["_id"])})
                return {"status": "SUCCESS", "result": "delete operation was successful"}

            elif query_type.lower() == "count":
                record_count = self.collection.count_documents(query)
                return {"status": "SUCCESS", "result": record_count}

            elif query_type.lower() == "aggregate":
                record_count = self.collection.aggregate(query)
                return {"status": "SUCCESS", "result": record_count}

        except Exception as exp:
            error_msg = "Error occurred while executing query on mongodb " + str(exp)
            return {"status": "FAILED", "error": error_msg}
