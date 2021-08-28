from src.client import Client
from src.exceptions import ApiError

def main():
    client = Client()
    #workflow
    client.retrieve_data()
    client.ingest_data()
    client.wrangle_output()
    try:
        resp = client.submit_data()
        print(resp.content.decode('utf-8'))
    except ApiError as e: 
        print(str(e))

if __name__ == '__main__':
    main()