from bs4 import BeautifulSoup
import re
import string
import operator
import csv

soup = BeautifulSoup(open("deep.html"))

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

with open('lecun.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(dict.items())

with open('lecun.csv', 'wb') as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames = ["name", "count"])
    writer.writeheader()

    with open('lecun.csv', 'rb') as incsv:
        reader = csv.reader(incsv)
        writer.writerows({'name': row[0], 'count': row[1]} for row in reader)

sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
print '----------------------------------------------------------------------------------'
print sorted_x


