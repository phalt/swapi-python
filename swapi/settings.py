# -*- coding: utf-8 -*-

'''
Settings and stuff.
'''

import os
DEBUG = bool(os.environ.get(('DEBUG'), False))
if DEBUG:
    BASE_URL = 'http://localhost:8000/api'
else:
    BASE_URL = 'http://swapi.dev/api'

PEOPLE = 'people'
PLANETS = 'planets'
STARSHIPS = 'starships'
VEHICLES = 'vehicles'
FILMS = 'films'
SPECIES = 'species'
