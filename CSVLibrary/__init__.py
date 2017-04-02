import csv
from robot.api import logger
from version import VERSION

__version__ = VERSION


class CSVLibrary(object):

    @staticmethod
    def _open_csv_file_for_read(filename, csv_reader=csv.reader, **kwargs):
        with open(filename, 'r') as csv_handler:
            reader = csv_reader(csv_handler, **kwargs)
            try:
                for row in reader:
                    yield row
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

    def read_csv_file_to_list(self, filename, delimiter=','):
        """Read CSV file and return its content as a Python list of tuples.
        
        - ``filename``:  name of csv file
        - ``delimiter``: Default: `,`
        """
        csv_list = self._open_csv_file_for_read(
            filename,
            csv_reader=csv.reader,
            delimiter=str(delimiter)
        )
        return [tuple(row) for row in csv_list]

    def read_csv_file_to_associative(self, filename, delimiter=',', fieldnames=None):
        """Read CSV file and return its content as a Python list of dictionaries.
        
        - ``filename``:  name of csv file
        - ``delimiter``: Default: `,`
        - ``fieldnames``: list of column names
        """
        csv_dict = self._open_csv_file_for_read(
            filename,
            csv_reader=csv.DictReader,
            delimiter=str(delimiter),
            fieldnames=fieldnames
        )
        return [item for item in csv_dict]

    def append_to_csv_file(self, filename, data):
        """This keyword will append data to a new or existing CSV file.
        
        - ``filename``:  name of csv file
        - ``data``: iterable(e.g. list or tuple) data.
        """
        if isinstance(data[0], dict):
            data = map(lambda row: row.items(), data)
        self._open_csv_file_for_write(filename, data=data, csv_writer=csv.writer)

    def csv_file_from_associative(self, filename, data, fieldnames=None, delimiter=','):
        """This keyword will create new file
        
        - ``filename``:  name of csv file
        - ``data``: iterable(e.g. list or tuple) data.
        - ``fieldnames``: list of column names
        - ``delimiter``: Default: `,`
        """
        fieldnames = fieldnames or data[0].keys()
        logger.console("fieldnames: %s" % fieldnames)
        self._open_csv_file_for_write(
            filename,
            data=data,
            csv_writer=csv.DictWriter,
            delimiter=str(delimiter),
            fieldnames=fieldnames
        )
