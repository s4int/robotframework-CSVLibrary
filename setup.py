#!/usr/bin/env python

from os.path import join, dirname, abspath
from setuptools import setup


def read(rel_path):
    here = abspath(dirname(__file__))
    with open(join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


REQUIREMENTS = read('requirements.txt').splitlines()
DESCRIPTION = read('README.md')

setup(name='robotframework-csvlibrary',
      version=get_version("CSVLibrary/__init__.py"),
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
      packages=['CSVLibrary'],
      )
