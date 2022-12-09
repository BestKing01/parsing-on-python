#Temirbayev Temirlan & Musabekov Bekzat

import requests
import json
import os
from bs4 import BeautifulSoup

url = "https://iitu.edu.kz/ru/people/"
req = requests.get(url)
src = req.text 

soup = BeautifulSoup(src, "lxml")
all_people = soup.find_all(class_ ="flex flex-col sm:h-48 rounded-md sm:grid grid-cols-3 shadow-lg flex-grow my-3 mx-3 cursor-pointer bg-white hover:shadow-2xl transition duration-500")

all_people_save = {}
for item in all_people:

    item_text = item.find("div", class_ = "text-gray-900 font-bold text-xl mb-2").text  
    item_href = item.get("href")
    
    print(f"{item_text}: {item_href}")

    all_people_save[item_href] = item_text


#Выводим всех людей, cсылки

with open ("all_people_save.json", "w", encoding='utf-8') as file:
    json.dump(all_people_save, file, indent=4, ensure_ascii=False)

# Сохраняем полностью ссылку и имя человека на csv файл
