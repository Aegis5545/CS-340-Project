from pymongo import MongoClient  # type: ignore
from bson.objectid import ObjectId  # type: ignore

class AnimalShelter():
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        USER = 'aacuser'
        PASS = 'SNHU4321'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30338
        DB = 'NEWAAC'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Creating C Method
    def create(self, data):
        if data is not None:
            try:
                insert_success = self.collection.insert_one(data)
                return insert_success.inserted_id is not None
            except Exception as e:
                print(f"An error has occurred: {e}")
        else:
            print("Data parameter is empty, cannot save")

    # Creating R method
    def read(self, searchData):
        if searchData is not None:
            try:
                data = list(self.collection.find(searchData, {"_id": False}))
                return data
            except Exception as e:
                print(f"An error has occurred: {e}")
                return []  # Return an empty list in case of error
        else:
            data = list(self.collection.find({}, {"_id": False}))
            return data

    # Creating U method
    def update(self, searchData, updateData):
        if searchData is not None:
            try:
                result = self.collection.update_many(searchData, {"$set": updateData})
                return result.raw_result
            except Exception as e:
                print(f"An error has occurred: {e}")
                return {}

    # Creating D method
    def delete(self, deleteData):
        if deleteData is not None:
            try:
                result = self.collection.delete_many(deleteData)
                return result.raw_result
            except Exception as e:
                print(f"An error has occurred: {e}")
                return {}
