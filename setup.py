#!/usr/bin/env python

from distutils.core import setup

setup(name='covid-date',
      version='1.0',
      description='Display the current Covid date',
      author='Jake Kara',
      author_email='jake@jakekara.com',
      url='https://jakekara.com',
      packages=['covid_date'],
      install_requires = [
        "pyyaml"
      ],
      entry_points = {
        'console_scripts': ['covid-date=covid_date.__main__:main'],
    }
)
