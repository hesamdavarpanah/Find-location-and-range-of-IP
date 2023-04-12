import pandas as pd
from netaddr import IPAddress, iprange_to_cidrs
from tqdm import tqdm
from mongodb_store import MongoDBStore
from ipinfo import getHandler

mongo = MongoDBStore()
db = mongo.create_database("ip2location")
mongo.create_collection(coll_name="all_data_collection")


class CSVReader:
    def db_csv_parser(self, db_filepath):
        db_dataframe = pd.read_csv(db_filepath,
                                   names=["ip_from_long", "ip_to_long", "country_code",
                                          "country_name", "region", "city", "latitude",
                                          "longitude", "zipcode", "timezone"],
                                   header=None)

        data = []
        for db_data in tqdm(db_dataframe.values, colour="green", desc="Loading IP2Location DB11.csv data"):
            ip_from = str(IPAddress(db_data[0]))
            cidr = str(iprange_to_cidrs(IPAddress(db_data[0]), IPAddress(db_data[1])).pop())
            data_dict = {
                "ip_from": ip_from,
                "ip_to": str(IPAddress(db_data[1])),
                "ip_from_long": db_data[0],
                "ip_to_long": db_data[1],
                "ip_cidr": cidr,
                "country_code": db_data[2],
                "country_name": db_data[3],
                "region": db_data[4],
                "city": db_data[5],
                "latitude": float(db_data[6]),
                "longitude": float(db_data[7]),
                "zipcode": db_data[8],
                "timezone": db_data[9]
            }
            data.append(data_dict)
        return data

    def asn_parser(self, data):
        lst = []
        asn_dataframe = pd.read_csv("files/IP2LOCATION-LITE-ASN.CSV",
                                    names=["ip_from_long", "ip_to_long", "cidr", "asn_number", "asn_name"],
                                    header=None)
        for doc in tqdm(data, colour="blue", desc="Merging asn data"):
            for asn_data in asn_dataframe.values:
                if doc["ip_from_long"] == asn_data[0] and doc["ip_to_long"] == asn_data[1]:
                    if not asn_data[3] == "-":
                        doc["asn_number"] = asn_data[3]
                    if not asn_data[4] == "-":
                        doc["asn_name"] = asn_data[4]
            lst.append(doc)
        return lst

    def iran_parser(self, data, access_token):
        lst = []
        for doc in tqdm(data[26_900:], colour="yellow", desc="Filtering selected data"):
            del doc["_id"]
            handler = getHandler(access_token=access_token, request_options={'timeout': 10800})
            ip_address = doc["ip_from"]
            details = handler.getDetails(ip_address)
            doc["ipinfo"] = details.all
            lst.append(doc)
        return lst
