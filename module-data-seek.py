#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 02:49:04 2022

@author: Vinicius Bispo and Pedro Calderaro
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager 
from selenium.webdriver.common.by import By


class WebScrapping:
    def __new__(self, link_data_seek):
        self.data = WebScrapping.DataSeek(link_data_seek)
        return self.data
    
    def DataSeek(link):
        service = Service(executable_path=(GeckoDriverManager().install()))
        option = Options()
        option.add_argument('--headless')
        try:
            browser = webdriver.Firefox(service=service, options=option)
            browser.get(link)
            table = browser.find_element(By.TAG_NAME, 'tbody')
            tags = table.find_elements(By.TAG_NAME, 'tr')
            print(browser.title)
            dataListFull = WebScrapping.dataExtraction(tags)
        except Exception:
            browser.close()
        return dataListFull
    
    def dataExtraction(rows_tags):
        dataList = [[], [], [], [], [], [], [], []]
        for i in range(len(rows_tags)):
                sections = rows_tags[i].find_elements(By.TAG_NAME, 'td')
                position = sections[0].text
                country = sections[1].text
                gdp = sections[2].text
                gdp1 = sections[3].text
                growth_rage = sections[4].text
                population = sections[5].text
                gdp_per_capita = sections[6].text
                share_of_world_gdp = sections[7].text
               
                dataList[0].append(position)
                dataList[1].append(country)
                dataList[2].append(gdp)
                dataList[3].append(gdp1)
                dataList[4].append(growth_rage)
                dataList[5].append(population)
                dataList[6].append(gdp_per_capita)
                dataList[7].append(share_of_world_gdp)
        return dataList
    
