===============================
swapi-python
===============================

.. image:: https://badge.fury.io/py/swapi.png
    :target: http://badge.fury.io/py/swapi

.. image:: https://travis-ci.org/phalt/swapi-python.png?branch=master
        :target: https://travis-ci.org/phalt/swapi-python

.. image:: https://pypip.in/d/swapi/badge.png
        :target: https://pypi.python.org/pypi/swapi


A Python helper library for swapi.co - the Star Wars API

NOTE: Tests will run against hosted API as opposed to data from github repo

* Free software: BSD license
* Documentation: https://swapi-python.readthedocs.org.

============
Installation
============

At the command line::

    $ pip install swapi

Basic Usage
========

To use swapi-python in a project::

    import swapi

All resources are accessible through the top-level ``get_resource()`` methods::

    luke = swapi.get_person(1)
    tatooine = swapi.get_planet(1)

Methods
=======

These are the top-level methods you can use to get resources from swapi.co. To learn more about the models and objects that are returned, see the ``models`` page.

get_person(id)
------------

Return a single ``Person`` resource.

Example::

    swapi.get_person(1)
    >>> <Person - Luke Skywalker>


get_planet(id)
------------

Return a single ``Planet`` resource.

Example::

    swapi.get_planet(1)
    >>> <Planet - Tatooine>


get_starship(id)
------------

Return a single ``Starship`` resource.

Example::

    swapi.get_starship(6)
    >>> <Starship - Death Star>


get_vehicle(id)
------------

Return a single ``Vehicle`` resource.

Example::

    swapi.get_vehicle(4)
    >>> <Vehicle - Sand Crawler>


get_film(id)
------------

Return a single ``Film`` resource.

Example::

    swapi.get_film(1)
    >>> <Film - A New Hope>


get_all("resource")
------------

Return a ``QuerySet`` containing all the items in a single resource. See the ```models``` page for more information on the models used in swapi-python.

Example::

    swapi.get_all("films")
    >>> <FilmQuerySet - 6>
