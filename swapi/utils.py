import requests
import ujson as json
try:
    from swapi import exceptions
except:
    import exceptions


def query(query):
    headers = {'User-Agent': 'swapi-python'}
    response = requests.get(query, headers=headers)
    if response.status_code != 200:
        raise exceptions.ResourceDoesNotExist('Resource does not exist')
    return response


def all_resource_urls(query):
    ''' Get all the URLs for every resource '''
    urls = []
    next = True
    while next:
        response = requests.get(query)
        json_data = json.loads(response.content)
        for resource in json_data['results']:
            urls.append(resource['url'])
        if bool(json_data['next']):
            query = json_data['next']
        else:
            next = False
    return urls
