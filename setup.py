#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'requests==2.5.0', 'six==1.8.0'
]

setup(
    name='swapi',
    version='0.1.1',
    description='A Python helper library for swapi.co - the Star Wars API',
    long_description=readme + '\n\n' + history,
    author='Paul Hallett',
    author_email='paulandrewhallett@gmail.com',
    url='https://github.com/phalt/swapi-python',
    packages=[
        'swapi',
    ],
    package_dir={'swapi':
                 'swapi'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='swapi',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
)
