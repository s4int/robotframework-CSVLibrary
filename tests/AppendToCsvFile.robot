*** Settings ***
Documentation    CSV examples for Robot Framework.
Library         Collections
Library         OperatingSystem
Library         CSVLibrary
Resource       testData.robot

*** Test Cases ***
Append list to empty file
    Empty Csv File  ${emptytFile}
    File Should Be Empty    ${emptytFile}
    Append To Csv File     ${emptytFile}    ${template_list}

    ${list}=  read csv file to list  ${emptytFile}
    Lists Should Be Equal  ${template_list}  ${list}
    [Teardown]    Remove File  ${emptytFile}

Append assoc to empty file
    Empty Csv File  ${emptytFile}
    File Should Be Empty    ${emptytFile}
    Append To Csv File     ${emptytFile}    ${template_dict}

    @{dict}=    Read Csv File To Associative  ${emptytFile}
    Dictionaries Should Be Equal  ${template_dict[-1]}  ${dict[-1]}
    [Teardown]    Remove File      ${emptytFile}

Append list to file with header
    [Setup]     Copy File	${inputFile}	${data_assoc_file}
    File Should Not Be Empty    ${data_assoc_file}
    Append To Csv File     ${data_assoc_file}    ${template_list}

    @{dict}=    Read Csv File To Associative  ${data_assoc_file}
    Dictionaries Should Be Equal  ${template_dict[-1]}  ${dict[-1]}
    [Teardown]    Remove File  ${data_assoc_file}

Append assoc to file with header
    [Setup]     Copy File	${inputFile}	${data_assoc_file}
    File Should Not Be Empty    ${data_assoc_file}
    Append To Csv File     ${data_assoc_file}    ${template_dict}

    @{dict}=    Read Csv File To Associative  ${data_assoc_file}
    Dictionaries Should Be Equal  ${template_dict[-1]}  ${dict[-1]}
    [Teardown]    Remove File  ${data_assoc_file}

Append single list row to file
    [Setup]     Copy File	${inputFile}	${data_assoc_file}
    File Should Not Be Empty    ${data_assoc_file}
    Append To Csv File     ${data_assoc_file}    ${template_row10}

    @{list}=    Read Csv File To List  ${data_assoc_file}
    Lists Should Be Equal  ${template_row10}  ${list[-1]}
    [Teardown]    Remove File  ${data_assoc_file}

Append single assoc row to file
    [Setup]     Copy File	${inputFile}	${data_assoc_file}
    File Should Not Be Empty    ${data_assoc_file}
    Append To Csv File     ${data_assoc_file}    ${template_dict_row10}

    @{dict}=    Read Csv File To Associative  ${data_assoc_file}
    Dictionaries Should Be Equal  ${template_dict_row10}  ${dict[-1]}
    [Teardown]    Remove File  ${data_assoc_file}
