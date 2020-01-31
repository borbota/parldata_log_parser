#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import re


	

f = open("src/search-2020-01-14T19_19_09Z.log", "r")
#reals = open(r"reals.txt", "w+")
#out = open(r"empties.txt","w+") 
test = open(r"test.txt","w+") 
with open("log_outfile.csv", "w") as csv_file:
	writer = csv.writer(csv_file, delimiter = ";")
	searchterm_counter = 0
	line_counter = 0
	myfilter_counter = 0
	#params_counter = 0
	empty_counter = 0
	fbclicid_counter = 0
	date_counter = 0
	both_search_and_filter_counter = 0
	newline = []
	for line in f.readlines():
		line_counter += 1
		date = re.findall(r'(?<=\[)(.*)(?= \+0000)', line)
		newline.append(date[0])

		#url1 = re.findall(r'(ftp:\/\/|www\.|https?:\/\/){1}[a-zA-Z0-9u00a1-\uffff0-]{2,}\.[a-zA-Z0-9u00a1-\uffff0-]{2,}(\S*)', line)
		#url2 = re.findall(r'(ftp:\/\/|www\.|https?:\/\/)[a-zA-Z0-9u00a1-ffff0-]{2,}[a-zA-Z0-9u00a1-\uffff0-](\S*)', line)
		
		search_term = re.findall(r'(?<=term=)(.*)(?=")', line)
		szuk_term = re.findall(r'(?<=term=)(.*)(?=%22)', line)
		if len(szuk_term) > 0:
			print(str(szuk_term[0]))
			test.write(str(szuk_term[0]) + "\n")
		#newline.append(search_term)
		
		myfilter = re.findall(r'(?<="{)(.*)(?=}")', line) # "{\x22id\x22:\x22filtered_query_v4\x22,\x22params\x22:{\x22q\x22:\x22privatiz\xC3\xA1ci\xC3\xB3\x22,\x22size\x22:20,\x22from\x22:0,\x22filter.date.from\x22:\x221900.01.01.\x22,\x22filter.date.to\x22:\x222019.11.\x22}}"
		#newline.append(myfilter)
		#params = re.findall(r'(?<="\\)(.*)(?=}")', line) 

		if "fbclid" in line:
			fb = 1
		else:
			fb = 0

		newline = []

		


test.close()
f.close()
#reals.close()
#out.close()

