#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_swapi.py
----------------------------------

Tests for `swapi` module.
"""

import unittest
import swapi

from swapi.models import (
    Starship,
    StarshipQuerySet,
    Film,
    FilmQuerySet,
    Vehicle,
    VehicleQuerySet,
    Planet,
    PlanetQuerySet,
    Species,
    SpeciesQuerySet,
    PeopleQuerySet
)

from swapi.utils import query
from swapi.exceptions import ResourceDoesNotExist
from swapi.settings import BASE_URL


class SwapiTest(unittest.TestCase):

    def test_get_all(self):
        people = swapi.get_all('people')
        self.assertEquals(people.count(), 82)
        self.assertEquals('<PeopleQuerySet - 82>', people.__repr__())

    def test_repr_(self):
        starship = swapi.get_starship(3)
        self.assertEquals('<Starship - Star Destroyer>', starship.__repr__())
        vehicle = swapi.get_vehicle(4)
        self.assertEquals('<Vehicle - Sand Crawler>', vehicle.__repr__())
        film = swapi.get_film(1)
        self.assertEquals('<Film - A New Hope>', film.__repr__())
        planet = swapi.get_planet(1)
        self.assertEquals('<Planet - Tatooine>', planet.__repr__())
        species = swapi.get_species(1)
        self.assertEquals('<Species - Human>', species.__repr__())

    def test_queryset_order_by(self):
        planets = swapi.get_all('planets')
        ordered = planets.order_by('diameter')
        self.assertEquals(ordered[0].diameter, '0')

        people = swapi.get_all('people')
        ordered = people.order_by('name')
        self.assertEquals(ordered[0].name, 'Ackbar')

    def test_get_person(self):
        luke = swapi.get_person(1)
        self.assertEquals(luke.name, "Luke Skywalker")
        self.assertEquals(
            '<Person - Luke Skywalker>', luke.__repr__())

    def test_get_person_starships(self):
        luke = swapi.get_person(1)
        starships = luke.get_starships()
        self.assertEquals(type(starships.items[0]), Starship)
        self.assertEquals(starships.__repr__(), "<StarshipQuerySet - 2>")

    def test_get_person_films(self):
        luke = swapi.get_person(1)
        films = luke.get_films()
        self.assertEquals(type(films.items[0]), Film)
        self.assertEquals(films.__repr__(), "<FilmQuerySet - 4>")

    def test_get_person_vehicles(self):
        luke = swapi.get_person(1)
        vehicles = luke.get_vehicles()
        self.assertEquals(type(vehicles.items[0]), Vehicle)
        self.assertEquals(vehicles.__repr__(), "<VehicleQuerySet - 2>")

    def test_get_person_homeworld(self):
        luke = swapi.get_person(1)
        home = luke.get_homeworld()
        tatooine = swapi.get_planet(1)
        self.assertEquals(type(home), Planet)
        self.assertEquals(home.name, tatooine.name)

    def test_get_person_species(self):
        luke = swapi.get_person(1)
        species = swapi.get_species(1)
        human = luke.get_species()
        self.assertEquals(type(species), Species)

    def test_species_get_people(self):
        species = swapi.get_species(1)
        self.assertEquals(type(species.get_people()), PeopleQuerySet)

    def test_species_get_films(self):
        species = swapi.get_species(1)
        self.assertEquals(type(species.get_films()), FilmQuerySet)

    def test_species_get_homeworld(self):
        species = swapi.get_species(1)
        self.assertEquals(type(species.get_homeworld()), Planet)

    def test_planet_get_films(self):
        planet = swapi.get_planet(1)
        self.assertEquals(type(planet.get_films()), FilmQuerySet)

    def test_planet_get_residents(self):
        planet = swapi.get_planet(1)
        self.assertEquals(type(planet.get_residents()), PeopleQuerySet)

    def test_film_get_characters(self):
        film = swapi.get_film(1)
        self.assertEquals(type(film.get_characters()), PeopleQuerySet)

    def test_film_get_starships(self):
        film = swapi.get_film(1)
        self.assertEquals(type(film.get_starships()), StarshipQuerySet)
        self.assertIn('<StarshipQuerySet - ', film.get_starships().__repr__())

    def test_film_get_vehicles(self):
        film = swapi.get_film(1)
        self.assertEquals(type(film.get_vehicles()), VehicleQuerySet)

    def test_film_get_planets(self):
        film = swapi.get_film(1)
        self.assertEquals(type(film.get_planets()), PlanetQuerySet)
        self.assertIn('<PlanetQuerySet - ', film.get_planets().__repr__())

    def test_film_get_species(self):
        film = swapi.get_film(1)
        self.assertEquals(type(film.get_species()), SpeciesQuerySet)
        self.assertIn('<SpeciesQuerySet - ', film.get_species().__repr__())

    def test_starship_get_films(self):
        starship = swapi.get_starship(3)
        self.assertEquals(type(starship.get_films()), FilmQuerySet)

    def test_starship_get_pilots(self):
        starship = swapi.get_starship(3)
        self.assertEquals(type(starship.get_pilots()), PeopleQuerySet)

    def test_vehicle_get_films(self):
        v = swapi.get_vehicle(4)
        self.assertEquals(type(v.get_films()), FilmQuerySet)

    def test_vehicle_get_pilots(self):
        v = swapi.get_vehicle(4)
        self.assertEquals(type(v.get_pilots()), PeopleQuerySet)

    def test_film_gen_crawl(self):
        film = swapi.get_film(1)
        for line in film.gen_opening_crawl():
            self.assertIn(line, film.opening_crawl)

    def test_raise_deliberate_exception(self):
        self.assertRaises(
            ResourceDoesNotExist,
            query,
            '{0}/people/123456/'.format(BASE_URL))
