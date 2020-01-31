from urllib import parse
import csv
import pandas as pd

f = open("src/search-2020-01-14T19_19_09Z.log", "r")

topusers = ["89.133.40.178", "178.48.162.223", "188.6.100.101", "188.156.217.28", "84.206.42.142", "213.229.183.42", "146.110.109.154", "94.21.164.93", "94.21.212.231"]

term_counts = dict()
ip_counts = dict()
speaker_filter_counts = dict()


lines = f.readlines()

for line in lines:
    url = line.split( )[10]
    ip = line.split( )[0]
    date= line.split( )[3][:12].replace('[', '')
    query = parse.parse_qs(parse.urlsplit(url).query)

    if (ip in topusers) or "Googlebot" in line: # if I want to filter for the topusers and bots
        pass
    else:
        # for terms
        try:
            word = str(query["term"][0].replace('[^a-zA-Z]', '').replace('"', ''))

            if len(word) > 0:
                if word in term_counts:
                    term_counts[word] += 1
                else:
                    term_counts[word] = 1
            else:
                pass
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

        if "fbclid" in line:
            fb = 1
        else:
            fb = 0

        if "Googlebot" in line:
            googlebot = 1
        else:
            googlebot = 0

        if ip in topusers:
            topuser = 1
        else:
            topuser = 0




#df = pd.DataFrame(list(ip_counts.items()), columns=['ip', 'count'])
#print(df.sort_values(["count"], ascending = False).head(20))
#df.to_csv("outfile_ips_without_topusers.csv", sep = "\t", index = False)


#df = pd.DataFrame(list(term_counts.items()), columns=['ip', 'count'])
#df.to_csv("outfile_terms_without_topusers.csv", sep = "\t", index = False)
#print(df.sort_values(["count"], ascending = False).head(20))


f.close()