
import os
import system

articles = open("articles.csv", "r")

lines = articles.readlines()

for line in lines:
    identifier = line.strip()
    sscript = "curl -X GET -L http://link.springer.com/" + identifier + ".pdf > article" + identifier.replace("/", "--") + ".pdf"
    os.system(sscript)
