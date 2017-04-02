*** Settings ***
Documentation    CSV examples for Robot Framework.
Library         Collections
Library         CSVLibrary

*** Variables ***
# Example data generated with: https://www.mockaroo.com/
@{template_list}=   1  Douglas  Morris  dmorris0@mozilla.org  Male  205.4.212.229
&{template_dict}=   id=1  first_name=Douglas  last_name=Morris  email=dmorris0@mozilla.org  gender=Male  ip_address=205.4.212.229


*** Test Cases ***
Read csv file to a list example test
    @{list}=  read csv file to list  ${CURDIR}${/}data.csv
    lists should be equal  ${template_list}  ${list[1]}

Read csv file to a dict example test
    @{dict}=    read csv file to associative  ${CURDIR}${/}data.csv
    dictionaries should be equal  ${template_dict}  ${dict[0]}
