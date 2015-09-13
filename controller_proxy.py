import sys
from store import Storer
from clean import Cleaner
from csv_dumper import CsvDumper

url_param = sys.argv[-1]

saved_page_loc=Storer.html_page(url_param)

Cleaner.start(saved_page_loc)

CsvDumper.start()


