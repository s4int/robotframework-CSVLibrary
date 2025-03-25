#!/usr/bin/env python
from setuptools import setup, find_packages
# from CSVLibrary.version import VERSION

with open('CSVLibrary/version.py') as f:
    VERSION = f.read().strip().lower().replace(" ", "").replace("\"", "").replace("version=", "")

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()

with open('README.md') as f:
    DESCRIPTION = f.read()

setup(name='robotframework-csvlibrary',
      version=VERSION,
      description='CSV library for Robot Framework',
      long_description=DESCRIPTION,
      long_description_content_type='text/markdown',
      author='Marcin Mierzejewski',
      author_email='<mmierz@gmail.com>',
      url='https://github.com/s4int/robotframework-CSVLibrary',
      license='Apache License 2.0',
      keywords='robotframework testing csv',
      platforms='any',
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing",
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
      ],
      install_requires=REQUIREMENTS,
      packages=find_packages(),
      )
