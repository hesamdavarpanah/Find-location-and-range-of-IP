from csv_ip_parser import CSVReader
from data_sender import IPSender
from mongodb_store import MongoDBStore
from pprint import pprint

csv = CSVReader()
mongo = MongoDBStore()

if __name__ == "__main__":
    mongo.create_database("ip2location")
    # mongo.create_collection("iran_data_collection")
    find = mongo.find_many(query=None, collection_name="iran_data_collection")
    sender = IPSender(data=find)
    # pprint(sender.country_data_sender())
    # pprint(sender.city_data_sender())
    # pprint(sender.province_data_sender())
    # pprint(sender.range_ip_sender())
    pprint(sender.single_ip_sender())
    # csv.db_csv_parser(db_filepath="files/IP2LOCATION-LITE-DB11.CSV")
    # insert = mongo.insert_many_data(data=csv.db_csv_parser(db_filepath="files/IP2LOCATION-LITE-DB11.CSV"))
    # print(insert)
    # find = mongo.find_many(collection_name="iran_asn", query=None)
    # insert = mongo.insert_many_data(data=csv.iran_parser(access_token="f5beaa7823aedd", data=find))
    # print(insert)
