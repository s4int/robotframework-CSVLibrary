
*** Variables ***
# Example data generated with: https://www.mockaroo.com/
@{template_row1}=   1   Douglas     Morris      dmorris0@mozilla.org    Male    205.4.212.229
@{template_row2}=   2   Stephanie   Oliver      soliver1@google.com.br  Female  18.101.154.106
@{template_row3}=   3   Russell     Castillo    rcastillo2@shop-pro.jp  Male    255.52.95.46
@{template_row4}=   4   Helen       Reed        hreed3@rambler.ru       Female  167.55.67.109
@{template_row5}=   5   Jesse       Wagner      jwagner4@histats.com    Male    252.37.62.215
@{template_row6}=   6   Ashley      Diaz        adiaz5@wikia.com        Female  79.87.105.139
@{template_row7}=   7   Rachel      Robinson    rrobinson6@blogger.com  Female  132.66.117.101
@{template_row8}=   8   Phillip     Johnston    pjohnston7@disqus.com   Male    70.152.55.21
@{template_row9}=   9   Craig       Burton      cburton8@toplist.cz     Male    73.117.157.82
@{template_row10}=  10  Patrick     Fisher      pfisher9@1und1.de       Male    2.36.191.97

@{template_list_dataFile}=  ${template_row1}    ${template_row2}    ${template_row3}
...     ${template_row4}    ${template_row5}    ${template_row6}

@{template_list}=       ${template_row7}   ${template_row8}    ${template_row9}
@{template_list_full}=  ${template_row1}    ${template_row2}    ${template_row3}
...     ${template_row4}    ${template_row5}    ${template_row6}
...     ${template_row7}   ${template_row8}    ${template_row9}

&{template_dict_row1}=      id=1   first_name=Douglas       last_name=Morris    email=dmorris0@mozilla.org      gender=Male     ip_address=205.4.212.229
&{template_dict_row2}=      id=2   first_name=Stephanie     last_name=Oliver    email=soliver1@google.com.br    gender=Female   ip_address=18.101.154.106
&{template_dict_row3}=      id=3   first_name=Russell       last_name=Castillo  email=rcastillo2@shop-pro.jp    gender=Male     ip_address=255.52.95.46
&{template_dict_row4}=      id=4   first_name=Helen         last_name=Reed      email=hreed3@rambler.ru         gender=Female   ip_address=167.55.67.109
&{template_dict_row5}=      id=5   first_name=Jesse         last_name=Wagner    email=jwagner4@histats.com      gender=Male     ip_address=252.37.62.215
&{template_dict_row6}=      id=6   first_name=Ashley        last_name=Diaz      email=adiaz5@wikia.com          gender=Female   ip_address=79.87.105.139
&{template_dict_row7}=      id=7   first_name=Rachel        last_name=Robinson  email=rrobinson6@blogger.com    gender=Female   ip_address=132.66.117.101
&{template_dict_row8}=      id=8   first_name=Phillip       last_name=Johnston  email=pjohnston7@disqus.com     gender=Male     ip_address=70.152.55.21
&{template_dict_row9}=      id=9   first_name=Craig         last_name=Burton    email=cburton8@toplist.cz       gender=Male     ip_address=73.117.157.82
&{template_dict_row10}=     id=10  first_name=Patrick       last_name=Fisher    email=pfisher9@1und1.de         gender=Male     ip_address=2.36.191.97

@{template_dict_dataFile}=  &{template_dict_row1}    &{template_dict_row2}    &{template_dict_row3}
...     &{template_dict_row4}    &{template_dict_row5}    &{template_dict_row6}

@{template_dict}=       &{template_dict_row7}    &{template_dict_row8}  &{template_dict_row9}
@{template_dict_full}=  &{template_dict_row1}    &{template_dict_row2}    &{template_dict_row3}
...     &{template_dict_row4}    &{template_dict_row5}    &{template_dict_row6}
...     &{template_dict_row7}    &{template_dict_row8}  &{template_dict_row9}

${csv_string_list}=          SEPARATOR=
...  1,Douglas,Morris,dmorris0@mozilla.org,Male,205.4.212.229\n
...  2,Stephanie,Oliver,soliver1@google.com.br,Female,18.101.154.106\n
...  3,Russell,Castillo,rcastillo2@shop-pro.jp,Male,255.52.95.46\n
...  4,Helen,Reed,hreed3@rambler.ru,Female,167.55.67.109\n
...  5,Jesse,Wagner,jwagner4@histats.com,Male,252.37.62.215\n
...  6,Ashley,Diaz,adiaz5@wikia.com,Female,79.87.105.139\n
...  7,Rachel,Robinson,rrobinson6@blogger.com,Female,132.66.117.101\n
...  8,Phillip,Johnston,pjohnston7@disqus.com,Male,70.152.55.21\n
...  9,Craig,Burton,cburton8@toplist.cz,Male,73.117.157.82\n

${csv_string_assoc}=          SEPARATOR=
...  id,first_name,last_name,email,gender,ip_address\n
...  1,Douglas,Morris,dmorris0@mozilla.org,Male,205.4.212.229\n
...  2,Stephanie,Oliver,soliver1@google.com.br,Female,18.101.154.106\n
...  3,Russell,Castillo,rcastillo2@shop-pro.jp,Male,255.52.95.46\n
...  4,Helen,Reed,hreed3@rambler.ru,Female,167.55.67.109\n
...  5,Jesse,Wagner,jwagner4@histats.com,Male,252.37.62.215\n
...  6,Ashley,Diaz,adiaz5@wikia.com,Female,79.87.105.139\n
...  7,Rachel,Robinson,rrobinson6@blogger.com,Female,132.66.117.101\n
...  8,Phillip,Johnston,pjohnston7@disqus.com,Male,70.152.55.21\n
...  9,Craig,Burton,cburton8@toplist.cz,Male,73.117.157.82\n

${csv_string_ext}=          SEPARATOR=
...  id,first_name,last_name,email,gender,ip_address\n
...  1,Douglas,Morris,dmorris0@mozilla.org,Male,205.4.212.229\n
...  2,Stephanie,Oliver,soliver1@google.com.br,Female,18.101.154.106\n
...  3,Russell,Castillo,rcastillo2@shop-pro.jp,Male,255.52.95.46\n
...  4,Helen,Reed,hreed3@rambler.ru,Female,167.55.67.109\n
...  5,Jesse,Wagner,jwagner4@histats.com,Male,252.37.62.215\n
...  6,Ashley,Diaz,adiaz5@wikia.com,Female,79.87.105.139\n
...  7,Rachel,Robinson,rrobinson6@blogger.com,Female,132.66.117.101\n
...  8,Phillip,Johnston,pjohnston7@disqus.com,Male,70.152.55.21\n
...  9,Craig,Burton,cburton8@toplist.cz,Male,73.117.157.82\n
...  10,Patrick,Fisher,pfisher9@1und1.de,Male,2.36.191.97\n

${emptytFile}=  ${CURDIR}${/}empty_file.csv
${inputFile}=   ${CURDIR}${/}data.csv
${data_create_file}=     ${CURDIR}${/}data_create.csv
${data_append_file}=    ${CURDIR}${/}data_append.csv

${data_assoc_file}=     ${CURDIR}${/}data_assoc.csv
${data_list_file}=    ${CURDIR}${/}data_list.csv

&{template_dict_quoting}=   id=1  first_name=Douglas  last_name=Morris  email=dmorris0@mozilla.org  gender="Male  ip_address=205.4.212.229
