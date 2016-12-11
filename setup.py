#!/usr/bin/env python

from setuptools import setup, find_packages
DESCRIPTION = "Notes API"

install_requires = [
    'eve>=0.7.dev0',
    'Flask-Script>=2.0.5',
    'Flask-Bootstrap>=3.3.7'
]

dependency_links = [
    'git+git://github.com/nicolaiarocci/eve.git'
]

setup(
    name='Notes-Api',
    versoin='0.1',
    description=DESCRIPTION,
    author='bosyotech',
    author_email='bosyotech.dev@gmail.com',
    url='https://github.com/amiel-marqeta/notes-api',
    install_requires=install_requires,
    dependency_links=dependency_links
)
