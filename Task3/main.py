from selenium import webdriver
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time



def start_selenium(url):
    # Settings of webdriver
    options = webdriver.ChromeOptions()
    # options.add_argument('--incognito')
    options.headless = True
    driver = uc.Chrome(options=options)
    driver.get(url)
    print("The browser was opened")
    try:
        driver.current_url
    except:
        print("The incorrect link")
        exit(0)
    return driver




def get_links():
    url = lambda \
        page: f'https://www.ozon.ru/category/telefony-i-smart-chasy-15501/?page={page}&sorting=rating'

    link_smartphone = []
    page = 1
    num_phones = 100

    driver = start_selenium(url(page))
    time.sleep(5)
    while True:
        driver.get(url(page))
        page += 1
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "lxml")
        all_char = soup.find_all("div", class_="k4r")
        for char in all_char:
            types = [i.text for i in char.find_all("font", color="#001a34")]
            if "Смартфон" in types:
                link = char.find('a', class_="tile-hover-target k8n").get("href")
                link_smartphone.append("https://www.ozon.ru" + link)
                if len(link_smartphone) == num_phones:
                    return driver, link_smartphone
        print(f"page = {page}, smartphone_links = {len(link_smartphone)}")


def get_info(driver, links):
    info = {}
    time.sleep(5)
    for num, link in enumerate(links):
        driver.get(link)
        print(f"The num link")
        time.sleep(5) 

        soup = BeautifulSoup(driver.page_source, "lxml")

        boxes = soup.find_all("div", class_="lx0")

        for box in boxes:
            if box.find("div", class_="xl0") and box.find("div", class_="xl0").text == "Основные":
                OS = box.find_all("dd", class_="lx3")[1].text
                if OS not in info:
                    info[OS] = 0
                info[OS] += 1
    driver.close()
    return info


if __name__ == "__main__":

    driver, links = get_links()

    info = get_info(driver, links)
    print(info)
