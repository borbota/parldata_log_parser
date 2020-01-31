from urllib import parse
import csv

f = open("src/search-2020-01-14T19_19_09Z.log", "r")

topusers = ["89.133.40.178", "178.48.162.223", "188.6.100.101", "188.156.217.28", "84.206.42.142", "213.229.183.42", "146.110.109.154", "94.21.164.93", "94.21.212.231"]
default_terms = ["korrupció", "emberi jogok", "költségvetés", "demokrácia", "soros györgy", "nato", "migráció or migráns", "euró", "kormányváltás"] # cards on page


lines = f.readlines()
with open("out/log_processed_logs.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter = "\t")
    header = ["ip", "date", "search_term", "speaker_filter", "fbclick", "googlebot", "superuser", "default_term"]
    writer.writerow(header)
    outfile_newline = []
    for line in lines:
        ip = line.split( )[0]
        date= line.split( )[3][:12].replace('[', '')
        url = line.split( )[10]
        query = parse.parse_qs(parse.urlsplit(url).query)

        outfile_newline.append(ip)
        outfile_newline.append(date)

        # for terms
        try:
            word = str(query["term"][0].replace('[^a-zA-Z]', '').replace('"', '')).lower()
        except KeyError:
            word = ""
        outfile_newline.append(word)

        # for speaker filters
        try:
            speaker = query["speaker_filter"][0].replace('[^a-zA-Z]', '').replace('"', '')
        except KeyError:
            speaker = ""
        outfile_newline.append(speaker)

        if "fbclid" in line:
            fb = 1
        else:
            fb = 0
        outfile_newline.append(fb)

        if "Googlebot" in line:
            googlebot = 1
        else:
            googlebot = 0
        outfile_newline.append(googlebot)

        if ip in topusers:
            topuser = 1
        else:
            topuser = 0
        outfile_newline.append(topuser)

        if word in default_terms:
            default_term = 1
        else:
            default_term = 0
        outfile_newline.append(default_term)

        print(outfile_newline)
        writer.writerow(outfile_newline)
        outfile_newline = []


f.close()