import csv
from robot.api import logger
from .version import VERSION
import sys

if sys.version_info.major >= 3:
    from io import StringIO as IO
else:
    from io import BytesIO as IO

__version__ = VERSION


class CSVLibrary(object):

    ROBOT_LIBRARY_VERSION = VERSION
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    @staticmethod
    def _reader(to_read, csv_reader=csv.reader, line_numbers=None, **kwargs):
        reader = csv_reader(to_read, **kwargs)
        try:
            for line_number, row in enumerate(reader):
                if line_numbers is None:
                    yield row
                elif isinstance(line_numbers, list) and line_number in line_numbers:
                    yield row
                    line_numbers.remove(line_number)
                    if len(line_numbers) == 0:
                        break
        except csv.Error as e:
            logger.error('line %d: %s' % (reader.line_num, e))

    def _open_csv_file_for_read(self, filename, csv_reader=csv.reader, line_numbers=None, **kwargs):
        if line_numbers is not None and isinstance(line_numbers, list):
            line_numbers = list(map(int, line_numbers))
        with open(filename, 'r') as csv_handler:
            return [row for row in self._reader(csv_handler, csv_reader, line_numbers, **kwargs)]

    def _read_csv(self, csv_string, csv_reader=csv.reader, line_numbers=None, **kwargs):
        if line_numbers is not None and isinstance(line_numbers, list):
            line_numbers = map(int, line_numbers)

        return [row for row in self._reader(csv_string.splitlines(), csv_reader, line_numbers, **kwargs)]

    @staticmethod
    def _open_csv_file_for_write(filename, data, csv_writer=csv.writer, **kwargs):

        if 'fieldnames' not in kwargs.keys() and isinstance(data[0], dict):
            kwargs['fieldnames'] = data[0].keys()

        with open(filename, 'a') as csv_handler:
            writer = csv_writer(csv_handler, **kwargs)
            try:
                if isinstance(writer, csv.DictWriter) and csv_handler.tell() == 0:
                    writer.writeheader()

                writer.writerows(data)
            except csv.Error as e:
                logger.error('file %s, %s' % (filename, e))

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
        return csv_list

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
        csv_list = self._read_csv(
            csv_string,
            csv_reader=csv.reader,
            delimiter=str(delimiter),
            **kwargs
        )
        return csv_list

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
        return csv_dict

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
        csv_dict = self._read_csv(
            csv_string,
            csv_reader=csv.DictReader,
            delimiter=str(delimiter),
            fieldnames=fieldnames,
            **kwargs
        )
        return csv_dict

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

        if isinstance(data, dict):
            data = [data]

        fieldnames = self._open_csv_file_for_read(
            filename,
            csv_reader=csv.reader,
            line_numbers=[0],
            **kwargs
        )[0]

        self._open_csv_file_for_write(
            filename,
            data=data,
            csv_writer=csv.DictWriter,
            fieldnames=fieldnames,
            **kwargs
        )

    def append_to_csv_string(self, csv_string, data, delimiter=',', **kwargs):
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

        fieldnames = self._read_csv(
            csv_string,
            csv_reader=csv.reader,
            delimiter=str(delimiter),
            **kwargs
        )[0]

        with IO() as output:
            if sys.version_info.major >= 3:
                output.write(csv_string)
            else:
                output.write(csv_string.encode("utf-8"))

            if 'fieldnames' not in kwargs.keys():
                kwargs['fieldnames'] = fieldnames
            if 'lineterminator' not in kwargs.keys():
                kwargs['lineterminator'] = '\n'

            writer = csv.DictWriter(output, **kwargs)
            writer.writerows(data)

            return output.getvalue()

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

    def csv_string_from_associative(self, data, fieldnames=None, delimiter=',', **kwargs):
        """This keyword will create new file

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

        if 'fieldnames' not in kwargs.keys():
            kwargs['fieldnames'] = fieldnames or data[0].keys()
        if 'lineterminator' not in kwargs.keys():
            kwargs['lineterminator'] = '\n'
        kwargs['delimiter'] = delimiter

        with IO() as output:
            writer = csv.DictWriter(output, **kwargs)
            writer.writeheader()
            writer.writerows(data)

            return output.getvalue()
