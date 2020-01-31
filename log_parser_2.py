from urllib import parse
import csv
import pandas as pd

f = open("src/search-2020-01-14T19_19_09Z.log", "r")

url_counts = dict()
ip_counts = dict()
speaker_filter_counts = dict()

lines = f.readlines()
for line in lines:
	url = line.split( )[10]
	ip = line.split( )[0]
	query = parse.parse_qs(parse.urlsplit(url).query)
	
	# for terms
	try:
		word = str(query["term"])
		if word in url_counts:
			url_counts[word] += 1
		else:
			url_counts[word] = 1
	except KeyError:
		pass

	# for ips
	if ip in ip_counts:
		ip_counts[ip] += 1
	else:
		ip_counts[ip] = 1

	# for speaker filters
	try:
		speaker = query["speaker_filter"][0].replace('[^a-zA-Z]', '').replace('"', '')
		if speaker in speaker_filter_counts:
			speaker_filter_counts[speaker] += 1
		else:
			speaker_filter_counts[speaker] = 1
	except KeyError:
		pass


df = pd.DataFrame(list(speaker_filter_counts.items()), columns=['speaker', 'count'])


#df.to_csv("outfile_speaker_filter_counts.csv", sep = "\t", index = False)
f.close()

"""with open('outfile.csv', 'w', newline="") as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in counts.items():
       writer.writerow([key, value])"""
