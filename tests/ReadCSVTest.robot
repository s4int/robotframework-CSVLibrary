*** Settings ***
Documentation    CSV examples for Robot Framework.
Library         Collections
Library         CSVLibrary

*** Variables ***
# Example data generated with: https://www.mockaroo.com/
@{template_list}=   1  Douglas  Morris  dmorris0@mozilla.org  Male  205.4.212.229
&{template_dict}=   id=1  first_name=Douglas  last_name=Morris  email=dmorris0@mozilla.org  gender=Male  ip_address=205.4.212.229
&{template_dict_quoting}=   id=1  first_name=Douglas  last_name=Morris  email=dmorris0@mozilla.org  gender="Male  ip_address=205.4.212.229
${csv_string}=          SEPARATOR=
...  id,first_name,last_name,email,gender,ip_address\n
...  1,Douglas,Morris,dmorris0@mozilla.org,Male,205.4.212.229\n
...  2,Stephanie,Oliver,soliver1@google.com.br,Female,18.101.154.106\n

*** Test Cases ***
Read csv file to a list example test
    @{list}=  read csv file to list  ${CURDIR}${/}data.csv
    lists should be equal  ${template_list}  ${list[1]}

Read csv file to a dict example test
    @{dict}=    read csv file to associative  ${CURDIR}${/}data.csv
    dictionaries should be equal  ${template_dict}  ${dict[0]}

Read csv file without quoting to associative
    @{dict}=    read csv file to associative  ${CURDIR}${/}data_quoting.csv  delimiter=,  quoting=${3}
    dictionaries should be equal  ${template_dict_quoting}  ${dict[0]}

Read csv string to a list example test
    @{list}=  read csv string to list  ${csv_string}
    lists should be equal  ${template_list}  ${list[1]}

Read csv string to a dict example test
    @{dict}=    read csv string to associative  ${csv_string}
    dictionaries should be equal  ${template_dict}  ${dict[0]}

