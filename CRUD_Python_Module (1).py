from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient to access the MongoDB databases
        # We use the verified Allied24 password here
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/?authSource=aac' % (username, password))
        self.database = self.client['aac']
        self.collection = self.database['animals']

    def create(self, data):
        # Insert a document and return True if successful
        if data is not None:
            try:
                self.collection.insert_one(data) 
                return True
            except Exception as e:
                print(f"Error: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        # Query for documents and return them as a list
        if query is not None:
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except Exception as e:
                print(f"Error: {e}")
                return []
        else:
            raise Exception("Query parameter is empty")
            # Update method (U in CRUD)
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            # Use update_many and $set as requested
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        else:
            return 0

    # Delete method (D in CRUD)
    def delete(self, query):
        if query is not None:
            # Use delete_many as requested
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            return 0
        