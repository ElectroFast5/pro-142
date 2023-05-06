from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome("C:/Users/terri/Desktop/C141/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        # BuautifulSoup object?
        soup=BeautifulSoup(browser.page_source, "html.parser")

        for ul_tag in soup.find_all("ul", atrrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            templist=[]

            for index, li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planets_data.append(temp_list)

    browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
           
scrape()

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

planet_df_1=pd.DataFrame(planets_data,columns=headers)

planet_df_1.to_csv("scraped_data.csv", index=True, index_label="id")