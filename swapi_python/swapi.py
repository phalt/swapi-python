import settings
from utils import query
from models import People


def get_all(resource):
    return ''


def get_planet(planet_id):
    return ''


def get_person(people_id):
    ''' Return a single person '''
    result = query("{0}/{1}/{2}/".format(
        settings.BASE_URL,
        settings.PEOPLE,
        unicode(people_id))
    )
    return People(result.content)


def get_starship(starship_id):
    return ''


def get_vehicle(vehicle_id):
    return ''


def get_species(species_id):
    return ''


def get_film(film_id):
    return ''



