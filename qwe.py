

import requests
import json
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    req = requests.get(url,verify=False)
    print (req.text) 
    #soup2 = BeautifulSoup(src, "lxml")
    
    # all_people_sdu = soup2.find_all("div", class_ = "abcfslMT10 abcfslF13")
    # for item in all_people_sdu:

    #     item_href = item.get("href")
    #     print(item_href)

#get_data(["https://iitu.edu.kz/ru/people/","https://kbtu.edu.kz/ru/faculties/faculty-of-information-technology/prepodavatelskij-sostav-fakulteta-informatsionnykh-tekhnologij","https://sdu.edu.kz/department-profile/","https://du.astanait.edu.kz/public","https://satbayev.university/ru/institutes/information-telecommunication-technologies"])
get_data("https://sdu.edu.kz/department-profile/")

#get_data("https://iitu.edu.kz/ru/people/")