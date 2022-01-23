*** Settings ***
Documentation    CSV examples for Robot Framework.
Library         Collections
Library         OperatingSystem
Library         CSVLibrary
Resource       testData.robot

*** Test Cases ***
Empty csv file
    [Setup]     Copy File	${CURDIR}${/}data.csv	${emptytFile}
    File Should Not Be Empty    ${emptytFile}
    Empty Csv File  ${emptytFile}
    File Should Be Empty    ${emptytFile}
    [Teardown]    Remove File  ${emptytFile}

Csv file from associative
    File Should Not Exist   ${data_create_file}
    Csv File From Associative  ${data_create_file}  ${template_dict_full}
    ${content}=  Get File    ${data_create_file}
    Should Be Equal     ${csv_string_assoc}  ${content}
    [Teardown]    Remove File  ${data_create_file}

Append to csv file
    [Setup]     Copy File	${CURDIR}${/}data.csv	${data_append_file}
    File Should Not Be Empty    ${data_append_file}
    ${aa}=  Append To Csv File  ${data_append_file}    ${template_dict}

    @{appended_dict}=    Read Csv File To Associative  ${data_append_file}
	Should Be Equal   ${appended_dict}  ${template_dict_full}
    [Teardown]    Remove File  ${data_append_file}

Append to csv string
	${content}=     Append To Csv String    ${csv_string_assoc}    ${template_dict_row10}
	Should Be Equal     ${csv_string_ext}  ${content}

CSV string from associative
	${content}=     Csv String From Associative    ${template_dict_full}
	Should Be Equal     ${csv_string_assoc}  ${content}
