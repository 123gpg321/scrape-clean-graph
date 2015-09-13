from bs4 import BeautifulSoup
import re
import string
import operator
import csv

class Cleaner:

	@staticmethod
	def start(path):
		soup = BeautifulSoup(open(path))

		print(soup.prettify())

		all_p=soup.find_all('p')

		all_p_str=str(all_p)

		cleaner = re.compile('<.*?>')

		cleantext = re.sub(cleaner,'', all_p_str)

		cleantext=cleantext.translate(string.maketrans('', ''), ',.')

		all_p_str_array=cleantext.split()

		dict = {}

		for sentence in all_p_str_array:
			for word in re.split('\s', sentence): # split with whitespace
				try:
				    dict[word] += 1
				except KeyError:
				    dict[word] = 1
		print dict

		for key, value in dict.items():
			if 0 < len(key) < 5:
				del dict[key]

		for key, value in dict.items():
			if value == 1:
				del dict[key]

		name_of_file=int(filter(str.isdigit, path))

		with open('./bubble_cloud/data/{}.csv'.format(name_of_file), 'wb') as outcsv:
			w = csv.DictWriter(outcsv, fieldnames = ["name", "count"])
			w.writeheader()
			w = csv.writer(outcsv)
			w.writerows(dict.items())
			
		sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
		print '----------------------------------------------------------------------------------'
		print sorted_x


