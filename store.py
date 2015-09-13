import urllib
import time

class Storer:

	@staticmethod
	def html_page(param):
		page_loc="./scraped_pages/{}.html".format(time.strftime("%Y%m%d%m%s"))
		urllib.urlretrieve("{}".format(param),page_loc)
    		return page_loc

