*** Settings ***
Documentation    CSV examples for Robot Framework.
Library         Collections
Library         ${CURDIR}${/}..${/}CSVLibrary

*** Variables ***
# Example data generated with: https://www.mockaroo.com/
@{template_list}=   1  Douglas  Morris  dmorris0@mozilla.org  Male  205.4.212.229
&{template_dict}=   id=1  first_name=Douglas  last_name=Morris  email=dmorris0@mozilla.org  gender=Male  ip_address=205.4.212.229
&{template_dict_quoting}=   id=1  first_name=Douglas  last_name=Morris  email=dmorris0@mozilla.org  gender="Male  ip_address=205.4.212.229

*** Test Cases ***
Read csv file to a list example test
    @{list}=  read csv file to list  ${CURDIR}${/}data.csv
    lists should be equal  ${template_list}  ${list[1]}

Read csv file to a dict example test
    @{dict}=    read csv file to associative  ${CURDIR}${/}data.csv
    dictionaries should be equal  ${template_dict}  ${dict[0]}

Read csv file to a dict example test access as attributes
    @{dict}=    read csv file to associative  ${CURDIR}${/}data.csv
    Should Be Equal As Strings    ${dict[0].first_name}    ${dict[0]}[first_name]
    Should Be Equal As Integers    ${dict[0].id}    ${dict[0]}[id]
    
Read csv file without quoting to associative
    @{dict}=    read csv file to associative  ${CURDIR}${/}data_quoting.csv  delimiter=,  quoting=${3}
    dictionaries should be equal  ${template_dict_quoting}  ${dict[0]}
