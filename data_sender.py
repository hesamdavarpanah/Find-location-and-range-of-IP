from pprint import pprint
from tqdm import tqdm
from netaddr import IPNetwork


class IPSender:
    def __init__(self, data):
        self.data = data

    def city_data_sender(self):
        city = []
        req_data = []
        for doc in self.data:
            city.append(doc["city"])
        set_list = set(city)
        for value in tqdm(set_list, desc="Parsing city data to valid format", colour="green"):
            data_dict = {
                "ontology": "ToutiyaKG24",
                "user": "automatic",
                "main_fields": [
                    {
                        "lang": "en",
                        "label": "",
                        "description": "",
                        "aliases": [],
                    }
                ],
                "instance_of": ["City"],
                "initial_source": ""
            }
            data_dict["main_fields"][0]["label"] = value
            req_data.append(data_dict)
        return req_data

    def country_data_sender(self):
        country = []
        req_data = []
        for doc in self.data:
            country.append(doc["country_name"])
        set_list = set(country)
        for value in tqdm(set_list, desc="Parsing country data to valid format", colour="blue"):
            data_dict = {
                "ontology": "ToutiyaKG24",
                "user": "automatic",
                "main_fields": [
                    {
                        "lang": "en",
                        "label": "",
                        "description": "",
                        "aliases": [],
                    }
                ],
                "instance_of": ["Country"],
                "initial_source": ""
            }
            data_dict["main_fields"][0]["label"] = value
            req_data.append(data_dict)
        return req_data

    def province_data_sender(self):
        province = []
        req_data = []
        for doc in self.data:
            province.append(doc["region"])
        set_list = set(province)
        for value in tqdm(set_list, desc="Parsing province data to valid format", colour="cyan"):
            data_dict = {
                "ontology": "ToutiyaKG24",
                "user": "automatic",
                "main_fields": [
                    {
                        "lang": "en",
                        "label": "",
                        "description": "",
                        "aliases": [],
                    }
                ],
                "instance_of": ["Province"],
                "initial_source": ""
            }
            data_dict["main_fields"][0]["label"] = value
            req_data.append(data_dict)
        return req_data

    def range_ip_sender(self):
        ip_cidr = []
        req_data = []
        for doc in tqdm(self.data):
            ip_cidr.append(doc["ip_cidr"])
        set_list = set(ip_cidr)
        for value in tqdm(set_list, desc="Parsing CIDR data to valid format", colour="white"):
            data_dict = {
                "ontology": "ToutiyaKG24",
                "user": "automatic",
                "main_fields": [
                    {
                        "lang": "en",
                        "label": "",
                        "description": "",
                        "aliases": [],
                    }
                ],
                "instance_of": ["RangeIP"],
                "initial_source": ""
            }
            data_dict["main_fields"][0]["label"] = value
            req_data.append(data_dict)
        return req_data

    def single_ip_sender(self):
        ip_cidr = []
        req_data = []
        for doc in tqdm(self.data, desc="Splitting CIDR data to single data", colour="yellow"):
            for ip in IPNetwork(doc["ip_cidr"]):
                ip_cidr.append(str(ip))
        set_list = set(ip_cidr)
        for value in tqdm(set_list, desc="Parsing single ip data to valid format", colour="black"):
            data_dict = {
                "ontology": "ToutiyaKG24",
                "user": "automatic",
                "main_fields": [
                    {
                        "lang": "en",
                        "label": "",
                        "description": "",
                        "aliases": [],
                    }
                ],
                "instance_of": ["SingleIP"],
                "initial_source": ""
            }
            data_dict["main_fields"][0]["label"] = value
            req_data.append(data_dict)
        return req_data
