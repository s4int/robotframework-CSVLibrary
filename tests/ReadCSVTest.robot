*** Settings ***
Documentation    CSV examples for Robot Framework.
Library         Collections
Library         CSVLibrary
Resource       testData.robot

*** Test Cases ***
Read csv file to a list example test
    @{list}=  Read Csv File To List  ${CURDIR}${/}data.csv
    Lists Should Be Equal  ${template_list_dataFile}  ${list[1:]}

Read csv file to a dict example test
    @{dict}=    Read Csv File To Associative  ${CURDIR}${/}data.csv
    Dictionaries Should Be Equal  ${template_dict_dataFile[-1]}  ${dict[-1]}

Read csv file to a dict example test access as attributes
    @{dict}=    Read Csv File To Associative  ${CURDIR}${/}data.csv
    Should Be Equal As Strings    ${template_dict_dataFile[-1].first_name}    ${dict[-1]}[first_name]
    Should Be Equal As Integers    ${template_dict_dataFile[-1].id}    ${dict[-1]}[id]
    
Read csv file without quoting to associative
    @{dict}=    Read Csv File To Associative  ${CURDIR}${/}data_quoting.csv  delimiter=,  quoting=${3}
    Dictionaries Should Be Equal  ${template_dict_quoting}  ${dict[0]}

Read csv string to a list example test
    @{list}=  Read Csv String To List  ${csv_string_list}
    Lists Should Be Equal  ${template_list_full}  ${list}

Read csv string to a dict example test
    @{dict}=    Read Csv String To Associative  ${csv_string_assoc}
    Dictionaries Should Be Equal  ${template_dict_full[-1]}  ${dict[-1]}
