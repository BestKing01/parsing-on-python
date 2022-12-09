#Temirbayev Temirlan & Musabekov Bekzat

import requests
import json
from bs4 import BeautifulSoup

def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }

    req0 = requests.get(url[0])
    src0 = req0.text 

    req1 = requests.get(url[1],verify=False)
    src1 = req1.text
    
    req2 = requests.get(url[2],verify=False)
    src2 = req2.text

    req3 = requests.get(url[3],verify=False)
    src3 = req3.text
    
    req4 = requests.get(url[4],verify=False)
    src4 = req4.text

    soup0 = BeautifulSoup(src0, "lxml")
    
    soup1 = BeautifulSoup(src1, "lxml")
    
    soup2 = BeautifulSoup(src2, "lxml")
    
    soup3 = BeautifulSoup(src3, "lxml")

    soup4 = BeautifulSoup(src4, "lxml")

    all_people_iitu = soup0.find_all(class_ ="flex flex-col sm:h-48 rounded-md sm:grid grid-cols-3 shadow-lg flex-grow my-3 mx-3 cursor-pointer bg-white hover:shadow-2xl transition duration-500")
    all_people_kbtu = soup1.find_all("div" ,class_ = "spoilers") 
    all_people_sdu = soup2.find_all("div", class_ = "abcfslMT10  abcfslF13")
    all_people_aitu = soup3.find_all("div", class_ = "ant-card-body")
    all_people_sat = soup4.find_all("div", class_ = "teacher_inner")
    
    all_people_iitu_save = {}

    for item in all_people_iitu:

        item_text = item.find("div", class_ = "text-gray-900 font-bold text-xl mb-2").text  
        item_href = item.get("href")
        all_people_iitu_save[item_href] = item_text
        
        print(all_people_iitu_save)
    
    all_people_kbtu_save = {}
    for item in all_people_kbtu:

        item_text = item.find("div", class_ = "desc").text
        all_people_kbtu_save[item_text]
        print(all_people_kbtu_save)
    
    # for item in all_people_sdu:
    #     item_href = item.get("href")
    #     print(item_href)

    # all_people_aitu_save ={}
    # for item in all_people_aitu:

    #     item_text = item.find("div", class_ = "ant-card-meta-detail").text  
    #     item_href = item.get("href")
    #     all_people_aitu_save[item_href] = item_text
        
    #     #print(all_people_iitu_save)
    
    all_people_sat_save = {}
    for item in all_people_sat:

        item_text = item.find("p").text
        all_people_sat_save = item_text
        
        print(all_people_sat_save)
        
        
    all_save = all_people_kbtu_save + all_people_iitu_save + all_people_sat_save

    with open ("all_people_save.json", "w", encoding='utf-8') as file:
        json.dump(all_save, file, indent=4, ensure_ascii=False)

    # with open ("all_people_save.json", "w", encoding='utf-8') as file:
    #     json.dump(all_people_save, file, indent=4, ensure_ascii=False)

    # all_people_save_href = {}

    # criteria =["Web","development","mobile","Java","программирование","ориентированное","Объектно","Объектно-ориентированное ","Алгоритмизация","Python","Разработка",
    #             "приложений","управления проектами ","Operating","systems","разработка",".NET","ASP.NET","Мобильная","data","science"]

    # for item in all_people_iitu:
    #     item_href = item.get("href")
    #     req = requests.get(item_href)
    #     src = req.text

    #     soup = BeautifulSoup(src, "lxml")

    #     find_box = soup.find("div", class_ = "flex-grow min-h-screen")

    #     post_img = "https://iitu.edu.kz/" + find_box.find("div", class_ = "h-64 w-64").find("img").get("src")
    #     post_name = find_box.find("div", class_ = "flex justify-center items-center flex-col").find("span", class_ = "text-3xl").text
    #     find_about = find_box.find('article', class_='my-5').text
        
    #     print(find_about)   

    #     final_text = post_name + '\n' + find_about + '\n' + post_img
    #     print (final_text)
    #     all_people_save_href[post_name] = find_about + post_img
    #     print(f"{post_name}: {find_about}: {post_img}")
        
    # with open ("all_people.json", "w", encoding='utf-8') as file:
    #     json.dump(all_people_save_href, file, indent=4, ensure_ascii=False)

get_data(["https://iitu.edu.kz/ru/people/","https://kbtu.edu.kz/ru/faculties/faculty-of-information-technology/prepodavatelskij-sostav-fakulteta-informatsionnykh-tekhnologij","https://sdu.edu.kz/department-profile/","https://du.astanait.edu.kz/public","https://satbayev.university/ru/institutes/information-telecommunication-technologies"])
#get_data("https://iitu.edu.kz/ru/people/")