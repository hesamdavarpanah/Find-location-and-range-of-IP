from tqdm import tqdm
from requests import post


class Requester:
    def __init__(self, data):
        self.data = data

    def post_request_sender(self, url):
        responses = []
        for json in tqdm(self.data, desc="Sending request", colour="green"):
            response = post(url, json=json)
            responses.append(response.text)
        return responses
