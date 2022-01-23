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
	lists should be equal  ${template_list}  ${list}
    [Teardown]    Remove File  ${emptytFile}

Append assoc to empty file
	Empty Csv File  ${emptytFile}
	File Should Be Empty    ${emptytFile}
	Append To Csv File     ${emptytFile}    ${template_dict}

    @{dict}=    read csv file to associative  ${emptytFile}
    dictionaries should be equal  ${template_dict[-1]}  ${dict[-1]}
	[Teardown]    Remove File      ${emptytFile}

Append list to file with header
	[Setup]     Copy File	${inputFile}	${data_assoc_file}
	File Should Not Be Empty    ${data_assoc_file}
	Append To Csv File     ${data_assoc_file}    ${template_list}

	@{dict}=    read csv file to associative  ${data_assoc_file}
    dictionaries should be equal  ${template_dict[-1]}  ${dict[-1]}
	[Teardown]    Remove File  ${data_assoc_file}

Append assoc to file with header
	[Setup]     Copy File	${inputFile}	${data_assoc_file}
	File Should Not Be Empty    ${data_assoc_file}
	Append To Csv File     ${data_assoc_file}    ${template_dict}

	@{dict}=    read csv file to associative  ${data_assoc_file}
    dictionaries should be equal  ${template_dict[-1]}  ${dict[-1]}
	[Teardown]    Remove File  ${data_assoc_file}
