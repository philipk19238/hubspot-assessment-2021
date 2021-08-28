import os 

class Configuration: 

    def __init__(self, api_key=None, dataset_endpoint=None, submit_endpoint=None): 
        self.API_KEY = api_key or os.getenv('API_KEY')
        self.DATASET_ENDPOINT = dataset_endpoint or os.getenv('DATASET_ENDPOINT')
        self.SUBMIT_ENDPOINT = submit_endpoint or os.getenv('SUBMIT_ENDPOINT')
        