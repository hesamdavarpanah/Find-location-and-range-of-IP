from csv_ip_parser import CSVReader
from data_sender import IPSender
from mongodb_store import MongoDBStore
from pprint import pprint

csv = CSVReader()
mongo = MongoDBStore()

if __name__ == "__main__":
    mongo.create_database("ip2location")
    find = mongo.find_many(query=None, collection_name="iran_data_collection")
    sender = IPSender(data=find)
    pprint(sender.single_ip_sender())
