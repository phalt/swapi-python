import requests
import exceptions

def query(query):
    result = requests.get(query)
    if result.status_code != 200:
        raise exceptions.ResourceDoesNotExist('Person does not exist')
    return result
