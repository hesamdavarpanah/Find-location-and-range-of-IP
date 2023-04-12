from pymongo import MongoClient, errors
from tqdm import tqdm

class MongoDBStore:
    def __init__(self):
        self.scheme = "mongodb"
        self.username = "admin"
        self.password = "admin"
        self.host = "192.168.13.166"
        self.port = 27017
        self.database = None
        self.collection = None

    @property
    def mongodb_uri(self):
        return f"{self.scheme}://{self.username}:{self.password}@{self.host}:{self.port}/"

    def create_database(self, db_name):
        try:
            client = MongoClient(self.mongodb_uri)
        except errors.InvalidURI as error:
            return error
        try:
            self.database = client[db_name]
            return self.database
        except errors.InvalidName as error:
            return error

    def create_collection(self, coll_name):
        try:
            self.collection = self.database[coll_name]
            return self.collection
        except errors.CollectionInvalid as error:
            return error

    def insert_one_data(self, data):
        try:
            self.collection.insert_one(data)
            return "The data inserted"
        except errors.InvalidDocument as error:
            return error

    def insert_many_data(self, data):
        try:
            insert = self.collection.insert_many(data)
            return f"{len(insert.inserted_ids)} data inserted"
        except errors.InvalidDocument as error:
            return error

    def update_many_data(self, old_query, new_query):
        try:
            self.collection.update_one(old_query, new_query)
        except ValueError as value_error:
            return value_error
        except errors.InvalidDocument as error:
            return error

    def find_many(self, collection_name, query):
        my_data = []
        coll = self.database[collection_name]
        try:
            if query:
                for data in tqdm(coll.find(query), desc="Finding data"):
                    my_data.append(data)
                return my_data
            else:
                for data in tqdm(coll.find(), desc="Finding data"):
                    my_data.append(data)
                return my_data
        except errors.InvalidDocument as error:
            return error
