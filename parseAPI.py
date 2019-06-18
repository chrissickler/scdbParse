# start at http://starcitizendb.com/api/ and loop thru each page
import json, urllib, os
from urllib.request import urlopen

urlParam = 'http://starcitizendb.com/api/'
urlMain = "http://starcitizendb.com"
# html = str(urlopen(url).read())
text_file = open("outputLOL.txt", "w")



def mainLoop(url):
    html = str(urlopen(url).read())
    for i in range(len(html) - 3):
        if html[i] == '<' and html[i+1] == 'a' and html[i+2] == ' ':
            pos = html[i:].find('</a>')
            string = html[i: i+pos+4]
            string = string.split("\"")
            string = urlMain + string[1]
            # here we check if the string is a link to a json file
            if ".json" not in string:
                mainLoop(string)
            else:
                print(string)
                text_file.write("%s\n" % string)


mainLoop(urlParam)