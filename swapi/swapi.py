try:
    from swapi import settings
    from swapi.utils import query, all_resource_urls
    from swapi.models import (
        People,
        PeopleQuerySet,
        Planet,
        PlanetQuerySet,
        Starship,
        StarshipQuerySet,
        Vehicle,
        VehicleQuerySet,
        Species,
        SpeciesQuerySet,
        Film,
        FilmQuerySet,
    )
except:
    import settings
    from utils import query, all_resource_urls
    from models import (
        People,
        PeopleQuerySet,
        Planet,
        PlanetQuerySet,
        Starship,
        StarshipQuerySet,
        Vehicle,
        VehicleQuerySet,
        Species,
        SpeciesQuerySet,
        Film,
        FilmQuerySet,
    )

def _get(id, type):
    ''' Return a single person '''
    result = query("{0}/{1}/{2}/".format(
        settings.BASE_URL,
        type,
        str(id))
    )
    return result


def get_all(resource):
    ''' Return all of a single resource '''
    QUERYSETS = {
        settings.PEOPLE: PeopleQuerySet,
        settings.PLANETS: PlanetQuerySet,
        settings.STARSHIPS: StarshipQuerySet,
        settings.VEHICLES: VehicleQuerySet,
        settings.SPECIES: SpeciesQuerySet,
        settings.FILMS: FilmQuerySet
    }

    urls = all_resource_urls(
        "{0}/{1}/".format(settings.BASE_URL, resource)
    )

    return QUERYSETS[resource](urls)


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
