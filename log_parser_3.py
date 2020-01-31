## version taking into account the ips too

from urllib import parse
import csv
import pandas as pd

f = open("src/search-2020-01-14T19_19_09Z.log", "r")

counts = dict()

lines = f.readlines()
for line in lines:
	ip = line.split( )[0]
	url = line.split( )[10]
	query = parse.parse_qs(parse.urlsplit(url).query)
	try:
		query_word = query["term"][0].replace('[^a-zA-Z]', '').replace('"', '')
		word = ip + "_" + query_word
		if len(word) > 0:
			if word in counts:
				counts[word] += 1
			else:
				counts[word] = 1
		else:
			print(word)
	except KeyError:
		pass

df = pd.DataFrame(list(counts.items()), columns=['ip_term', 'count'])

s = df["ip_term"].apply(lambda x: x.split('_'))
df["ip"] = s.apply(lambda x: x[0])
df["term"] = s.apply(lambda x: x[1])

del df["ip_term"]

#df.to_csv("outfile_ips_and_terms_with_counts.csv", sep = "\t", index = False)

"""
with open('outfile_2.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in counts.items():
       writer.writerow([key, value])
"""
f.close()