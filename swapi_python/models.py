import json
import six
from utils import query


class BaseModel(object):

    def __init__(self, raw_data):
        json_data = json.loads(raw_data)
        for key, value in six.iteritems(json_data):
            setattr(self, key, value)


class BaseQuerySet(object):

    def __init__(self):
        self.items = []


class StarshipQuerySet(BaseQuerySet):

    def __init__(self, list_of_urls):
        super(StarshipQuerySet, self).__init__()
        for url in list_of_urls:
            response = query(url)
            self.items.append(Starship(response.content))

    def __repr__(self):
        return '<StarshipQuerySet - {0}>'.format(str(len(self.items)))

class Starship(BaseModel):

    def __init__(self, raw_data):
        super(Starship, self).__init__(raw_data)

    def __repr__(self):
        return '<Starship - {0}>'.format(self.name)

class People(BaseModel):
    ''' Representing a single person '''

    def __init__(self, raw_data):
        super(People, self).__init__(raw_data)

    def __repr__(self):
        return '<Person - {0}>'.format(self.name)

    def get_starships(self):
        return StarshipQuerySet(self.starships)
