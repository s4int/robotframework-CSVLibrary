import csv
from robot.api import logger


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
        """
        with open(filename, "w") as csv_handler:
            csv_handler.truncate()

    def read_csv_file_to_list(self, filename, delimiter=','):
        """Read CSV file and return its content as a Python list of tuples.
        """
        csv_list = self._open_csv_file_for_read(
            filename,
            csv_reader=csv.reader,
            delimiter=delimiter
        )
        return [tuple(row) for row in csv_list]

    def read_csv_file_to_associative(self, filename, delimiter=',', fieldnames=None):
        """Read CSV file and return its content as a Python list of dictionaries.
        """
        csv_dict = self._open_csv_file_for_read(
            filename,
            csv_reader=csv.DictReader,
            delimiter=delimiter,
            fieldnames=fieldnames
        )
        return csv_dict

    def append_to_csv_file(self, filename, data):
        """This keyword will append data to a new or existing CSV file.
        Data should be iterable (e.g. list or tuple)
        """
        if isinstance(data[0], dict):
            data = map(lambda row: row.items(), data)
        self._open_csv_file_for_write(filename, data=data, csv_writer=csv.writer)

    def csv_file_from_associative(self, filename, data, fieldnames=None, delimiter=','):
        """This keyword will create new file
        """
        fieldnames = fieldnames or data[0].keys()
        logger.console("fieldnames: %s" % fieldnames)
        self._open_csv_file_for_write(
            filename,
            data=data,
            csv_writer=csv.DictWriter,
            delimiter=delimiter,
            fieldnames=fieldnames
        )
