import json, urllib, os
# import requests
# from bs4 import BeautifulSoup

from urllib.request import urlopen

url = 'http://starcitizendb.com/api/ships/specs'
urlMain = "http://starcitizendb.com"
html = str(urlopen(url).read())
text_file = open("ShipLinkOutput.txt", "w")

for i in range(len(html) - 3):
    if html[i] == '<' and html[i+1] == 'a' and html[i+2] == ' ':
        pos = html[i:].find('</a>')
        string = html[i: i+pos+4]
        string = string.split("\"")
        string = urlMain + string[1]
        # print(string)
        text_file.write("%s\n" % string)
text_file.close
text_file= open("ShipLinkOutput.txt", "r")
lines = text_file.read().split('\n')
# print(len(lines))
curr_dir = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.join(curr_dir, 'output')
# print(dest_dir)

for line in lines:
    if line != '':
        response = urllib.request.urlopen(line)
        data = json.loads(response.read())
        spl = line.split("/")
        strName = spl[len(spl)-1]
        # print(strName)
        path = os.path.join(dest_dir, strName)
        # print(path)
        with open(path, 'w') as outfile:
            json.dump(data, outfile)

text_file.close()


