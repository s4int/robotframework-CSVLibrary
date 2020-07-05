import csv
from robot.api import logger
from .version import VERSION

__version__ = VERSION


class CSVLibrary(object):

    ROBOT_LIBRARY_VERSION = VERSION
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    @staticmethod
    def _open_csv_file_for_read(filename, csv_reader=csv.reader, line_numbers=None, **kwargs):
        if line_numbers is not None and isinstance(line_numbers, list):
            line_numbers = map(int, line_numbers)
        with open(filename, 'r') as csv_handler:
            reader = csv_reader(csv_handler, **kwargs)
            try:
                for line_number, row in enumerate(reader):
                    if line_numbers is None:
                        yield row
                    elif isinstance(line_numbers, list):
                        if line_number in line_numbers:
                            yield row
                            line_numbers.remove(line_number)
                            if len(line_numbers) == 0:
                                break
            except csv.Error as e:
                logger.error('file %s, line %d: %s' % (filename, reader.line_num, e))

    @staticmethod
    def _open_csv_file_for_write(filename, data, csv_writer=csv.writer, **kwargs):
        with open(filename, 'ab') as csv_handler:
            writer = csv_writer(csv_handler, **kwargs)
            try:
                if isinstance(writer, csv.DictWriter) and 'fieldnames' in kwargs.keys():
                    csv_handler.truncate()
                    writer.writeheader()

                writer.writerows(data)
            except csv.Error as e:
                logger.error('file %s, line %d: %s' % (filename, writer.line_num, e))

    @staticmethod
    def empty_csv_file(filename):
        """This keyword will empty the CSV file.
        
        - ``filename``: name of csv file
        """
        with open(filename, "w") as csv_handler:
            csv_handler.truncate()

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
        csv_list = self._open_csv_file_for_read(
            filename,
            csv_reader=csv.reader,
            delimiter=str(delimiter),
            **kwargs
        )
        return [tuple(row) for row in csv_list]

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
        csv_dict = self._open_csv_file_for_read(
            filename,
            csv_reader=csv.DictReader,
            delimiter=str(delimiter),
            fieldnames=fieldnames,
            **kwargs
        )
        return [item for item in csv_dict]

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
        if isinstance(data[0], dict):
            data = map(lambda row: row.items(), data)
        self._open_csv_file_for_write(filename, data=data, csv_writer=csv.writer, **kwargs)

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
        fieldnames = fieldnames or data[0].keys()
        self._open_csv_file_for_write(
            filename,
            data=data,
            csv_writer=csv.DictWriter,
            delimiter=str(delimiter),
            fieldnames=fieldnames,
            **kwargs
        )
