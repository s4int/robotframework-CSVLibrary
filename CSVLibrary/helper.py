import csv
import sys
import os
from pathlib import Path

from robot.api import logger
from robot.utils.dotdict import DotDict

if sys.version_info.major >= 3:
    from io import StringIO as IO
else:
    from io import BytesIO as IO


class DotDictReader(csv.DictReader):
    def __next__(self):
        return DotDict(super().__next__())


class Helper(object):

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

    def _read_csv(self, csv_handler, csv_reader=csv.reader, line_numbers=None, **kwargs):
        if line_numbers is not None and isinstance(line_numbers, list):
            line_numbers = list(map(int, line_numbers))

        return [row for row in self._reader(csv_handler, csv_reader, line_numbers, **kwargs)]

    def _open_csv_file_for_read(self, filename, csv_reader=csv.reader, line_numbers=None, **kwargs):
        with open(filename, 'r') as csv_handler:
            return self._read_csv(csv_handler, csv_reader, line_numbers, **kwargs)

    @staticmethod
    def _write_csv(csv_handler, data, csv_writer=csv.writer, **kwargs):
        if 'fieldnames' not in kwargs.keys() and isinstance(data[0], dict):
            kwargs['fieldnames'] = data[0].keys()

        writer = csv_writer(csv_handler, **kwargs)
        try:
            if isinstance(writer, csv.DictWriter) and csv_handler.tell() == 0:
                writer.writeheader()

            if not isinstance(data[0], (list, tuple, dict, set)):
                data = [data]
            writer.writerows(data)
        except csv.Error as e:
            logger.error('%s' % e)

    def _open_csv_file_for_write(self, filename, data, csv_writer=csv.writer, **kwargs):
        open_args = {'mode': 'ab'}
        if sys.version_info >= (3, 2):
            open_args['mode'] = 'a'
            open_args['newline'] = ''

        with open(filename, **open_args) as csv_handler:
            self._write_csv(csv_handler, data, csv_writer, **kwargs)

    def _get_io(self):
        return IO
    
    # CSV Merge
    def _fetch_matching_files(self,
            csv_input: str,
            file_filter: str
        ):
        # If given -> apply file filter
        pattern = "*.csv"
        if file_filter:
            pattern = f"*{file_filter}*.csv"

        # Fetch all given files / files in given directory
        if len(csv_input) == 1 and Path(csv_input[0]).resolve().is_dir():
            csv_files = sorted(Path(csv_input[0]).rglob(pattern))
        else:
            csv_files = [Path(p) for p in csv_input]
        if not csv_files:
            raise ValueError(f"No CSV files found for given input: {csv_input}")
        return csv_files
    
    # CSV Merge
    def _write_to_csv(self,
            output_file: str,
            rows: list,
            header: list[str] = None,
            delelte_file: bool = True
        ):
        if delelte_file:
            os.remove(output_file) if os.path.exists(output_file) else None

        with open(output_file, "w", newline='', encoding="utf-8") as fout:
            writer = csv.writer(fout)
            if header:
                writer.writerow(header)
            writer.writerows(rows)
            logger.info(f"File '{output_file}' has been written successfully!")
