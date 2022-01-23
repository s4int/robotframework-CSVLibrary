*** Settings ***
Documentation    CSV examples for Robot Framework.
Library         Collections
Library         CSVLibrary
Resource       testData.robot

*** Test Cases ***
Append list to empty string
	${emptyString}=     Set Variable    ${EMPTY}
	${out}=  Append To Csv String     ${emptyString}    ${template_list}
	Should Be Equal  ${csv_string_list}  ${out}

Append assoc to empty string
	${emptyString}=     Set Variable    ${EMPTY}
	${out}=  Append To Csv String     ${emptyString}    ${template_dict}
	Should Be Equal  ${csv_string_assoc}  ${out}

Append list to string with header
	${out}=  Append To Csv String     ${csv_string_assoc}    ${template_list}

	@{list}=  Read Csv String To List  ${out}
    lists should be equal  ${template_list[-1]}  ${list[-1]}

Append assoc to string with header
	${out}=  Append To Csv String     ${csv_string_assoc}    ${template_dict_row3}

	@{dict}=  Read Csv String to Associative  ${out}
    Dictionaries Should Be Equal  ${template_dict_row3}  ${dict[-1]}
