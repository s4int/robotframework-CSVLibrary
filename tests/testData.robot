
*** Variables ***
# Example data generated with: https://www.mockaroo.com/
@{template_row1}=   7   Rachel      Robinson    rrobinson6@blogger.com  Female  132.66.117.101
@{template_row2}=   8   Phillip     Johnston    pjohnston7@disqus.com   Male    70.152.55.21
@{template_row3}=   9   Craig       Burton      cburton8@toplist.cz     Male    73.117.157.82
@{template_row4}=   10  Patrick     Fisher      pfisher9@1und1.de       Male    2.36.191.97
@{template_list}=   ${template_row1}    ${template_row2}    ${template_row3}

&{template_dict_row1}=   id=7   first_name=Rachel   last_name=Robinson  email=rrobinson6@blogger.com    gender=Female  ip_address=132.66.117.101
&{template_dict_row2}=   id=8   first_name=Phillip  last_name=Johnston  email=pjohnston7@disqus.com     gender=Male    ip_address=70.152.55.21
&{template_dict_row3}=   id=9   first_name=Craig    last_name=Burton    email=cburton8@toplist.cz       gender=Male    ip_address=73.117.157.82
&{template_dict_row4}=   id=10  first_name=Patrick  last_name=Fisher    email=pfisher9@1und1.de         gender=Male    ip_address=2.36.191.97
@{template_dict}=       &{template_dict_row1}    &{template_dict_row2}  &{template_dict_row3}

${csv_string_list}=          SEPARATOR=
...  7,Rachel,Robinson,rrobinson6@blogger.com,Female,132.66.117.101\n
...  8,Phillip,Johnston,pjohnston7@disqus.com,Male,70.152.55.21\n
...  9,Craig,Burton,cburton8@toplist.cz,Male,73.117.157.82\n

${csv_string_assoc}=          SEPARATOR=
...  id,first_name,last_name,email,gender,ip_address\n
...  7,Rachel,Robinson,rrobinson6@blogger.com,Female,132.66.117.101\n
...  8,Phillip,Johnston,pjohnston7@disqus.com,Male,70.152.55.21\n
...  9,Craig,Burton,cburton8@toplist.cz,Male,73.117.157.82\n

${emptytFile}=  ${CURDIR}${/}empty_file.csv
${inputFile}=   ${CURDIR}${/}data.csv

${data_assoc_file}=     ${CURDIR}${/}data_assoc.csv
${data_list_file}=    ${CURDIR}${/}data_list.csv
