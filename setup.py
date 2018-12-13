#!/usr/bin/env python

from os.path import join, dirname
from setuptools import setup

version_path=join(dirname(__file__), 'CSVLibrary', 'version.py')
with open(version_path) as f:
    exec(compile(f.read(), version_path, 'exec'))

DESCRIPTION = """
CSV file support for Robot Framework.
"""[1:-1]

setup(name         = 'robotframework-csvlibrary',
      version      = VERSION,
      description  = 'CSV library for Robot Framework',
      long_description = DESCRIPTION,
      author       = 'Marcin Mierzejewski',
      author_email = '<mmierz@gmail.com>',
      url          = 'https://github.com/s4int/robotframework-CSVLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing csv',
      platforms    = 'any',
      classifiers  = [
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2",
	  "Programming Language :: Python :: 3",
          "Topic :: Software Development :: Testing"
      ],
      install_requires = [
          'robotframework >= 2.6.0',
      ],
      packages    = ['CSVLibrary'],
      )
