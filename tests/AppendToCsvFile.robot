*** Settings ***
Documentation    CSV examples for Robot Framework.
Library         Collections
Library         OperatingSystem
Library         CSVLibrary

*** Variables ***
# Example data generated with: https://www.mockaroo.com/
@{template_row}=   1  Douglas  Morris  dmorris0@mozilla.org  Male  205.4.212.229
@{template_list}=   ${template_row}
&{template_dict}=   id=1  first_name=Douglas  last_name=Morris  email=dmorris0@mozilla.org  gender=Male  ip_address=205.4.212.229

${csv_string}=          SEPARATOR=
...  id,first_name,last_name,email,gender,ip_address\n
...  1,Douglas,Morris,dmorris0@mozilla.org,Male,205.4.212.229\n
...  2,Stephanie,Oliver,soliver1@google.com.br,Female,18.101.154.106\n
${emptytFile}=  ${CURDIR}${/}empty_file.csv
${inputFile}=   ${CURDIR}${/}data.csv

${data_assoc_file}=     ${CURDIR}${/}data_assoc.csv
${data_list_file}=    ${CURDIR}${/}data_list.csv


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
    dictionaries should be equal  ${template_dict}  ${dict[0]}
	[Teardown]    Remove File      ${emptytFile}

Append list to file with header
	[Setup]     Copy File	${inputFile}	${data_assoc_file}
	File Should Not Be Empty    ${data_assoc_file}
	Append To Csv File     ${data_assoc_file}    ${template_list}

	@{dict}=    read csv file to associative  ${data_assoc_file}
    dictionaries should be equal  ${template_dict}  ${dict[-1]}
	[Teardown]    Remove File  ${data_assoc_file}

Append assoc to file with header
	[Setup]     Copy File	${inputFile}	${data_assoc_file}
	File Should Not Be Empty    ${data_assoc_file}
	Append To Csv File     ${data_assoc_file}    ${template_dict}

	@{dict}=    read csv file to associative  ${data_assoc_file}
    dictionaries should be equal  ${template_dict}  ${dict[-1]}
	[Teardown]    Remove File  ${data_assoc_file}
