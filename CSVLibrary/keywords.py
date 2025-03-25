import csv
import sys
from pathlib import Path
import os

from robot.api import logger
from robot.api.deco import library, keyword
from .helper import Helper, DotDictReader
from .version import VERSION


@library
class Keywords(object):

    ROBOT_LIBRARY_VERSION = VERSION
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.helper = None
        self.IO = None

    @property
    def kw(self):
        self.helper = Helper()
        return self.helper

    @property
    def io(self):
        self.IO = self.helper._get_io()
        return self.IO

    @staticmethod
    @keyword(tags=["CSVLibrary"])
    def empty_csv_file(filename):
        """This keyword will empty the CSV file.

        - ``filename``: name of csv file
        """
        with open(filename, "w") as csv_handler:
            csv_handler.truncate()

    @keyword(tags=["CSVLibrary"])
    def read_csv_file_to_list(self, filename, delimiter=',', **kwargs):
        """Read CSV file and return its content as a Python list of tuples.

        - ``filename``:  name of csv file
        - ``delimiter``: Default: `,`
        - ``line_numbers``: List of linenumbers to read. Default None
        - ``quoting`` (int):
          _0_: QUOTE_MINIMAL
          _1_: QUOTE_ALL
          _2_: QUOTE_NONNUMERIC
          _3_: QUOTE_NONE
        """
        csv_list = self.kw._open_csv_file_for_read(
            filename,
            csv_reader=csv.reader,
            delimiter=str(delimiter),
            **kwargs
        )
        return csv_list

    @keyword(tags=["CSVLibrary"])
    def read_csv_string_to_list(self, csv_string, delimiter=',', **kwargs):
        """Read CSV string and return its content as a Python list of tuples.

        - ``csv_string``:  name of csv file
        - ``delimiter``: Default: `,`
        - ``line_numbers``: List of linenumbers to read. Default None
        - ``quoting`` (int):
          _0_: QUOTE_MINIMAL
          _1_: QUOTE_ALL
          _2_: QUOTE_NONNUMERIC
          _3_: QUOTE_NONE
        """
        if sys.version_info.major < 3:
            csv_string = csv_string.encode("utf-8")

        with self.io(csv_string) as csv_handler:
            csv_list = self.kw._read_csv(
                csv_handler,
                csv_reader=csv.reader,
                delimiter=str(delimiter),
                **kwargs
            )
            return csv_list

    @keyword(tags=["CSVLibrary"])
    def read_csv_file_to_associative(self, filename, delimiter=',', fieldnames=None, **kwargs):
        """Read CSV file and return its content as a Python list of dictionaries.

        - ``filename``:  name of csv file
        - ``delimiter``: Default: `,`
        - ``fieldnames``: list of column names
        - ``line_numbers``: List of linenumbers to read. Default None
        - ``quoting`` (int):
          _0_: QUOTE_MINIMAL
          _1_: QUOTE_ALL
          _2_: QUOTE_NONNUMERIC
          _3_: QUOTE_NONE
        """
        kwargs['fieldnames'] = fieldnames
        csv_dict = self.kw._open_csv_file_for_read(
            filename,
            csv_reader=DotDictReader,
            delimiter=str(delimiter),
            **kwargs
        )
        return csv_dict

    @keyword(tags=["CSVLibrary"])
    def read_csv_string_to_associative(self, csv_string, delimiter=',', fieldnames=None, **kwargs):
        """Read CSV from string  and return its content as a Python list of dictionaries.

        - ``csv_string``:  csv formatted string
        - ``delimiter``: Default: `,`
        - ``fieldnames``: list of column names
        - ``line_numbers``: List of linenumbers to read. Default None
        - ``quoting`` (int):
          _0_: QUOTE_MINIMAL
          _1_: QUOTE_ALL
          _2_: QUOTE_NONNUMERIC
          _3_: QUOTE_NONE
        """
        if sys.version_info.major < 3:
            csv_string = csv_string.encode("utf-8")

        with self.io(csv_string) as csv_handler:
            csv_dict = self.kw._read_csv(
                csv_handler,
                csv_reader=DotDictReader,
                delimiter=str(delimiter),
                fieldnames=fieldnames,
                **kwargs
            )
            return csv_dict

    @keyword(tags=["CSVLibrary"])
    def append_to_csv_file(self, filename, data, **kwargs):
        """This keyword will append data to a new or existing CSV file.

        - ``filename``:  name of csv file
        - ``data``: iterable(e.g. list or tuple) data.
        - ``quoting`` (int):
          _0_: QUOTE_MINIMAL
          _1_: QUOTE_ALL
          _2_: QUOTE_NONNUMERIC
          _3_: QUOTE_NONE
        """

        header = self.kw._open_csv_file_for_read(
            filename,
            csv_reader=csv.reader,
            line_numbers=[0],
            **kwargs
        )

        if isinstance(data, dict):
            data = [data]

        fieldnames = None
        if isinstance(data[0], dict):
            fieldnames = data[0].keys()

        if isinstance(data[0], dict) and len(header) > 0:
            fieldnames = header[0]

        if fieldnames is not None:
            kwargs['fieldnames'] = fieldnames
            kwargs['csv_writer'] = csv.DictWriter

        self.kw._open_csv_file_for_write(
            filename,
            data=data,
            **kwargs
        )

    @keyword(tags=["CSVLibrary"])
    def append_to_csv_string(self, csv_string, data, **kwargs):
        """This keyword will append data to a new or existing CSV string.

        - ``csv_string``:  csv formatted string
        - ``data``: iterable(e.g. list or tuple) data.
        - ``quoting`` (int):
          _0_: QUOTE_MINIMAL
          _1_: QUOTE_ALL
          _2_: QUOTE_NONNUMERIC
          _3_: QUOTE_NONE
        """
        if isinstance(data, dict):
            data = [data]

        if 'lineterminator' not in kwargs.keys():
            kwargs['lineterminator'] = '\n'

        if sys.version_info.major < 3:
            csv_string = csv_string.encode("utf-8")

        with self.io(csv_string) as csv_handler:
            header = self.kw._read_csv(
                csv_handler,
                csv_reader=csv.reader,
                **kwargs
            )

            fieldnames = None
            if isinstance(data[0], dict):
                fieldnames = data[0].keys()

            if isinstance(data[0], dict) and len(header) > 0:
                fieldnames = header[0]

            if fieldnames is not None:
                kwargs['fieldnames'] = fieldnames
                kwargs['csv_writer'] = csv.DictWriter

            self.kw._write_csv(csv_handler, data, **kwargs)
            return csv_handler.getvalue()

    @keyword(tags=["CSVLibrary"])
    def csv_file_from_associative(self, filename, data, fieldnames=None, delimiter=',', **kwargs):
        """This keyword will create new file

        - ``filename``:  name of csv file
        - ``data``: iterable(e.g. list or tuple) data.
        - ``fieldnames``: list of column names
        - ``delimiter``: Default: `,`
        - ``quoting`` (int):
          _0_: QUOTE_MINIMAL
          _1_: QUOTE_ALL
          _2_: QUOTE_NONNUMERIC
          _3_: QUOTE_NONE
        """
        kwargs['fieldnames'] = fieldnames or data[0].keys()

        self.kw._open_csv_file_for_write(
            filename,
            data=data,
            csv_writer=csv.DictWriter,
            delimiter=str(delimiter),
            **kwargs
        )

    @keyword(tags=["CSVLibrary"])
    def csv_string_from_associative(self, data, fieldnames=None, delimiter=',', **kwargs):
        """This keyword will return csv string

        - ``data``: iterable(e.g. list or tuple) data.
        - ``fieldnames``: list of column names
        - ``delimiter``: Default: `,`
        - ``quoting`` (int):
          _0_: QUOTE_MINIMAL
          _1_: QUOTE_ALL
          _2_: QUOTE_NONNUMERIC
          _3_: QUOTE_NONE
        """
        if isinstance(data, dict):
            data = [data]

        kwargs['fieldnames'] = fieldnames or data[0].keys()
        if 'lineterminator' not in kwargs.keys():
            kwargs['lineterminator'] = '\n'
        kwargs['delimiter'] = delimiter

        with self.io() as csv_handler:
            self.kw._write_csv(csv_handler, data, csv_writer=csv.DictWriter, **kwargs)
            return csv_handler.getvalue()

    @keyword(tags=["CSVLibrary"])
    def merge_csv_files(self,
            *csv_input: str,
            output_file: str,
            file_filter: str = None
        ):
        """
        Keyword to merge multiple equivalent CSV files to one common CSV output file.

        = Arguments =
        ``csv_input (str)`` -> the folder or exact files you want to merge.\n
        ``output_file (str)`` -> the path & name of your output file.\n
        ``file_filter (str)`` -> regex pattern to merge only files with specific file name.\n

        = Use Case =
        A lot of data is downloaded from your data storage & its downloaded into multiple CSV files for reasons 
        like these files are separated into different folders with their related timestamp.\n
        Due to having the same data set & table headers, it makes sense to merge csv files for further csv data validation.

        = Example =
        Merge all files in ${DOWN_DIR}:
        |    Merge Csv Files     ${DOWN_DIR}\\    output_file=MergedCustomData.csv

        Merge all files in ${DOWN_DIR} with name *weather_date*:
        |    Merge Csv Files     ${DOWN_DIR}\\    output_file=MergedCustomData.csv    file_filter=weather_data

        Merge exactly two CSV files:
        |    Merge Csv Files     
        |    ...    ${DOWN_DIR}\\Folder01\\data.csv
        |    ...    ${DOWN_DIR}\\Folder02\\data.csv
        |    ...    MergedCustomData.csv
        """
        # Fetch matching files from file system
        csv_files = self.kw._fetch_matching_files(csv_input, file_filter)
        
        # Merge found files
        all_rows = []
        header = None
        for csv_file in csv_files:
            logger.debug(f"Merging file '{csv_file}'")
            with open(csv_file, "r", encoding="utf-8") as fin:
                lines = fin.readlines()

            fixed_lines = []
            for line in lines:
                # If mistakenly quotes are started but not ended in a linke lik "start & end"
                # -> fix it (needed due to occurance in example tests)
                quote_count = line.count('"')
                if quote_count % 2 != 0:
                    line = line.replace('"', '""')
                fixed_lines.append(line.strip())
            reader = csv.reader(fixed_lines)

            try:
                file_header = next(reader)
            except Exception as e:
                logger.warn(f"Invalid Header: {e}")
                continue

            if header is None:
                header = file_header
            elif header != file_header:
                raise ValueError(f"Only CSV Files with same structure / headers can be merged!")

            for row_num, row in enumerate(reader, start=2):
                if len(row) != len(header):
                    logger.info(f"Row Nr. {row_num} in File {csv_file} is skipped - count of columns does not match: {row}")
                    continue
                all_rows.append(row)

        if not header:
            raise ValueError("No valid header found!")

        # If continously increasing ID column is used, it will be recongized during merge
        if  header[0].lower() == "id":
            for i, row in enumerate(all_rows, start=1):
                row[0] = str(i)

        # Write content to csv file
        self.kw._write_to_csv(output_file, all_rows, header)