# -*- coding: utf-8 -*-

__author__ = 'Paul Hallett'
__email__ = 'paulandrewhallett@gmail.com'
__version__ = '0.1.0'

from .swapi import (
    get_all,
    get_person,
    get_planet,
    get_starship,
    get_vehicle,
    get_film,
    get_species
)

from .settings import (
    PEOPLE,
    PLANETS,
    STARSHIPS,
    VEHICLES,
    FILMS,
    SPECIES
)
