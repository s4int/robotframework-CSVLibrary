*** Settings ***
Library    CSVLibrary


*** Test Cases ***
Merge Files from a Folder
    Merge Csv Files
    ...    ${CURDIR}\\..\\Examples
    ...    output_file=01_merged.csv

Merge Files from a Folder to specific path
    Merge Csv Files
    ...    ${CURDIR}\\..\\Examples
    ...    output_file=${CURDIR}\\02_merged.csv

Merge Files from a Folder with File Filter (Pattern)
    Merge Csv Files
    ...    ${CURDIR}\\..\\Examples
    ...    output_file=03_merged.csv
    ...    file_filter=data

Merge Exact two files
    Merge Csv Files
    ...    ${CURDIR}\\..\\Examples\\data_quoting.csv
    ...    ${CURDIR}\\..\\Examples\\data.csv
    ...    output_file=04_merged.csv