# Robot Framework CSVLibrary
## Introduction

This is a temporarly CSVLibrary version which supports python 3. It is intended to be used until [this pull request](https://github.com/s4int/robotframework-CSVLibrary/pull/7) is pulled. 

CSVLibrary is a [Robot Framework](http://robotframework.org/) library for handling csv files.

More information about this library can be found in the [Keyword Documentation](https://rawgit.com/juacompe/robotframework-CSVLibrary/master/doc/CSVLibrary.html).

## Installation
### Using pip
```bash
      pip install -U robotframework-csvlibrary-py3
```

### Manual installation
1. Make sure you have [Robot Framework installed](http://code.google.com/p/robotframework/wiki/Installation).
2. Download source distributions (`*.tar.gz`) for the library and its dependencies:
      - https://pypi.python.org/pypi/robotframework-csvlibrary-py3
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
