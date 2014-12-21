====
Models
====

Swapi-python uses custom models to handle single resources and collections of resources in a native and pythonic way.

This page documents the extra methods and functions of those classes.


Single Resource Model
=====================

A single resource model maps all the standard attributes for a resource as properties on the object. For example, a ``People`` resource has a ``name`` and ``height`` attribute. These can be accessed with swapi-python as properties, like so::

    luke = swapi.get_person(1)
    luke.name
    >>> u'Luke Skywalker'
    luke.height
    >>> u'172'


Getting Related Resources
-------------------------

Each resource model has specific methods for getting back the collection of resources related to it. For example, the People resource can have Starship Resources linked to it. With swapi-python you can get those resources like so::

    luke = swapi.get_person(1)
    ships = luke.get_starships()

Each resource model has slightly different methods. Multiple resources return a Multiple Collection Model (see below).

People
------
* ``get_starships()``
Return the starships that this person has piloted.

* ``get_vehicles()``
Return the vehicles that this person has piloted.

* ``get_homeworld()``
Get the homeworld of this person.

* ``get_species()``
Return the species of this person.

* ``get_films()``
Return the films that this person has been in.

Species
-------
* ``get_films()``
Return the films that this species has been in.

* ``get_people()``
Return the people who are a member of this species.

* ``get_homeworld()``
Return the homeworld of this species.

Planet
-------
* ``get_residents()``
Return the people who live on this planet.

* ``get_films()``
Return the films that this planet has appeared in.

Starship
--------
* ``get_pilots()``
Return the pilots of this starship.

* ``get_films()``
Return the films that this starship has been in.

Vehicle
-------
* ``get_pilots()``
Return the pilots of this vehicle.

* ``get_films()``
Return the films that this vehicle has been in.

Film
----
* ``get_starships()``
Get the starships in this film.

* ``get_characters()``
Get the characters in this film.

* ``get_vehicles()``
Get the vehicles in this film.

* ``get_planets()``
Get the planets in this film.

* ``get_species()``
Get the species in this film.

* ``gen_opening_crawl()``
A generator yielding each line of the opening crawl for this film.

* ``print_crawl()``
A novelty method that prints out each line of the opening crawl with a 0.5 second delay between each line.


Multiple Collection Model
=========================

When you query swapi.co for multiple resources of the same type, they will be returned as a ``ResourceQuerySet``, which is a collection of those resources that you requested. For example, to get the ``Starship`` resources linked to a person, you can do the following::

    luke = swapi.get_person(1)
    starships = luke.get_starships()
    >>> <StarshipQuerySet - 2>

``ResourceQuerySet`` models have additional methods for dealing with multiple resources.

The items are accessible as the ``item`` property on the ResourceQuerySet if you want to directly access them::

    starships.items
    >>> [<Starship - X-wing>, <Starship - Lambda Shuttle>]

.order_by("attribute")
----------------------

Return the list of Single Resource Models in this collection, ordered by a particular attribute. For example::

    planets = swapi.get_all("planets")
    for p in planets.order_by("diameter"):
        print(p.name)

This will return the planets ordered by their diameter.

This method will try to turn the attribute into an interger before ordering them, as most resources are unicode strings. If you try to order by string, it will order it alphabetically. Please be aware that for string ordering it might not always come out as you would expect.

.count()
-------

Return a count of the number of items in this collection..

.iter()
-------

An iterable method that can be used to iterate over each item in this collection::

    for v in vehicles.iter():
        print(v.name)
