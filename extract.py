import requests
import csv
from bs4 import BeautifulSoup
import re
import json

def extraction(YEAR):
    URL = f"https://en.wikipedia.org/wiki/{YEAR}"

    x = requests.get(URL)
    data=[]

    page = BeautifulSoup(x.text, 'html.parser')
    event = page.find("span", id="Events").parent
    month = event.find_next_sibling("ul")
    for i in range (14):
        #print(month.parent.find("h3").find("span").text)
        data.append({"Month No.":f"{i+1}","Month-Day(s)-Events":[re.sub("\[([^\]]+)\]","",tag.text) for tag in month.find_all("li")]})
        month = month.find_next_sibling("ul")

    print(data)

    file = f"Data/{YEAR}.json"
    try:
        with open(file,'w') as fp:
            json.dump(data, fp)

    # csv_file = f"Data/{YEAR}.csv"
    # try:
    #     with open(csv_file, 'w', encoding="utf-8") as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames = ["Month No.","Month-Day(s)-Events"])
    #         writer.writeheader()
    #         for key in data:
    #             writer.writerow(key)

    except IOError:
        print("Writing Error")

#YEAR=1900
#extraction(YEAR)