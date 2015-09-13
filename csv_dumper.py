class CsvDumper:

	@staticmethod
	def start():
		import re
		import json
		csv_filenames=[]
		rootdir='/home/gpg/projects/piksel/scrape-clean-graph/bubble_cloud/data'
		import os
		for file in os.walk(rootdir):
			csv_filenames.append(file)

		list(csv_filenames[0])

		a=list(csv_filenames[0])

		a[2]

		clean_csv_filenames=[]
		for i in a[2]:
			if (isinstance(i, basestring) and i.endswith('.csv')):
				clean_csv_filenames.append(i)
		
		digits_only=[]
		
		for i in clean_csv_filenames:
			b=re.findall('\d+', i)
			if b:
				digits_only.append(b[0])

		latest_timestamp=max(digits_only)

		latest_csv=str(latest_timestamp) + '.csv'

		csv_filename={'csv':latest_csv}
		
		with open('./bubble_cloud/latest_csv.json', 'w') as fp:
    			json.dump(csv_filename, fp)
