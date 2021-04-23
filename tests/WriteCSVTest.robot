*** Settings ***
Documentation    CSV examples for Robot Framework.
Library         Collections
Library         OperatingSystem
Library         CSVLibrary

*** Variables ***
# Example data generated with: https://www.mockaroo.com/
@{template_list}=   1  Douglas  Morris  dmorris0@mozilla.org  Male  205.4.212.229
&{template_dict_row1}=   id=1  first_name=Douglas  last_name=Morris  email=dmorris0@mozilla.org  gender=Male  ip_address=205.4.212.229
&{template_dict_row2}=   id=2  first_name=Stephanie  last_name=Oliver  email=soliver1@google.com.br  gender=Female  ip_address=18.101.154.106
@{template_dict_rows}=  &{template_dict_row1}   &{template_dict_row2}

&{template_dict_append}=  ip_address=255.36.191.0  id=11  first_name=John  last_name=ParkerFisher  email=jparker00@google.com  gender=Male

${csv_string}=          SEPARATOR=
...  id,first_name,last_name,email,gender,ip_address\n
...  1,Douglas,Morris,dmorris0@mozilla.org,Male,205.4.212.229\n
...  2,Stephanie,Oliver,soliver1@google.com.br,Female,18.101.154.106\n
${data_empty_copy}=     ${CURDIR}${/}data_copy.csv
${data_create_file}=     ${CURDIR}${/}data_create.csv
${data_append_file}=    ${CURDIR}${/}data_append.csv

*** Test Cases ***
Empty csv file
    [Setup]     Copy File	${CURDIR}${/}data.csv	${data_empty_copy}
    File Should Not Be Empty    ${data_empty_copy}
    Empty Csv File  ${data_empty_copy}
    File Should Be Empty    ${data_empty_copy}
    [Teardown]    Remove File  ${data_empty_copy}

Csv file from associative
    File Should Not Exist   ${data_create_file}
    Csv File From Associative  ${data_create_file}  ${template_dict_rows}
    ${content}=  Get File    ${data_create_file}
    Should Be Equal     ${csv_string}  ${content}
    [Teardown]    Remove File  ${data_create_file}

Append to csv file
    [Setup]     Copy File	${CURDIR}${/}data.csv	${data_append_file}
    File Should Not Be Empty    ${data_append_file}
    ${aa}=  Append To Csv File  ${data_append_file}    ${template_dict_append}

    @{appended_dict}=    read csv file to associative  ${data_append_file}
	List Should Contain Value   ${appended_dict}  ${template_dict_append}
    [Teardown]    Remove File  ${data_append_file}
