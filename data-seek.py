"""
Created on Fri Jul 15 00:08:10 2022

@author: vinicius bispo and Pedro Caleze
"""

from selenium import webdriver 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

service = Service(executable_path=(GeckoDriverManager().install()))
option = Options()
option.add_argument('--headless')
option.add_argument()
link_to_data_seek = "https://www.worldometers.info/gdp/gdp-by-country/"

# We recommend that you download the page to your computer and place the path in the variable: 
# link_to_data_seek = "./GDP_by_Country_-_Worldometer.html"

try:
    browser = webdriver.Firefox(service=service, options=option)
    site = browser.get(link_to_data_seek)
    table = browser.find_element(By.TAG_NAME, 'tbody')
    tags = table.find_elements(By.TAG_NAME, 'tr')
    print(browser.title)
    for i in range(len(tags)):
        sections = tags[i].find_elements(By.TAG_NAME, 'td')
        position = sections[0].text
        country = sections[1].text
        gdp = sections[2].text
        gdp1 = sections[3].text
        growth_rage = sections[4].text
        population = sections[5].text
        gdp_per_capita = sections[6].text
        share_of_world_gdp = sections[7].text
        print(f"{i+1}# Country | {country}")
except Exception:
    browser.close()
