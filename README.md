[![Build Status](https://app.travis-ci.com/s4int/robotframework-CSVLibrary.svg?branch=master)](https://app.travis-ci.com/s4int/robotframework-CSVLibrary)
[![Build Status](https://img.shields.io/pypi/v/robotframework-CSVLibrary.svg?label=version)](https://pypi.python.org/pypi/robotframework-CSVLibrary)

# Robot Framework CSVLibrary
## Introduction
CSVLibrary is a [Robot Framework](http://robotframework.org/) library for handling csv files.

More information about this library can be found in the [Keyword Documentation](https://rawgit.com/s4int/robotframework-CSVLibrary/master/doc/CSVLibrary.html).

## Installation
### Using pip
```bash
      pip install -U robotframework-csvlibrary
```

### Manual installation
1. Make sure you have [Robot Framework installed](http://code.google.com/p/robotframework/wiki/Installation).
2. Download source distributions (`*.tar.gz`) for the library and its dependencies:
      - https://pypi.python.org/pypi/robotframework-csvlibrary
3. Extract each source distribution to a temporary location.
4. Go each created directory from the command line and install each project using:

```bash
      python setup.py install
```

## Example

Basic example:
```robotframework
*** Settings ***
Library                     Collections
Library                     CSVLibrary
    
*** Test Cases ***
Read csv file to a list example test
  @{list}=  read csv file to list  data.csv
  Log  ${list[0]}
  Log  ${list[1]}

Read csv file to a dict example test
  @{dict}=    read csv file to associative  data.csv
  Log  &{dict[0]}[first_name]  &{dict[0]}[last_name]
```
