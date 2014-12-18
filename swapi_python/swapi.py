import settings
from utils import query
from models import (
    People,
    Planet,
    Starship,
    Vehicle,
    Species,
    Film
)


def _get(id, type):
    ''' Return a single person '''
    result = query("{0}/{1}/{2}/".format(
        settings.BASE_URL,
        type,
        unicode(id))
    )
    return result

def get_all(resource):
    return ''


def get_planet(planet_id):
    ''' Return a single planet '''
    result = _get(planet_id, settings.PLANETS)
    return Planet(result.content)


def get_person(people_id):
    ''' Return a single person '''
    result = _get(people_id, settings.PEOPLE)
    return People(result.content)


def get_starship(starship_id):
    ''' Return a single starship '''
    result = _get(starship_id, settings.STARSHIPS)
    return Starship(result.content)


def get_vehicle(vehicle_id):
    ''' Return a single vehicle '''
    result = _get(vehicle_id, settings.VEHICLES)
    return Vehicle(result.content)


def get_species(species_id):
    ''' Return a single species '''
    result = _get(species_id, settings.SPECIES)
    return Species(result.content)


def get_film(film_id):
    ''' Return a single film '''
    result = _get(film_id, settings.FILMS)
    return Film(result.content)



