from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pandas as pd

class world_cup_schedule_scraper:
    def __init__(self):
        
        self.attr = 'on'
        # wcs = world_cup_schedule_scraper()

    def get_raw_schedule_tables_from_website(url):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        res_html = driver.execute_script('return document.body.innerHTML')
        soup = BeautifulSoup(res_html,'html.parser') #beautiful soup object to be used for parsing html content
        mytables = soup.find_all("table")     
        return mytables

    # def get_schedule_tables_from_website(self,url):
    #     wcs.get_js_soup(url,self.driver)
    #     mytables = sup.find_all("table")
    #     return mytables

    def clean_web_tables_to_df(raw_tables_object):
        list_of_tables = []
        for i in range(0,len(raw_tables_object)):
            var = (raw_tables_object[i].findAll(text='Match No'))
            if len(var) > 0:
                
                df = pd.read_html(str(raw_tables_object[i]))
                list_of_tables.append(df[0])

        first_table = list_of_tables[0]
        clean_schedule_df = first_table[pd.to_numeric(first_table['Match No'], errors='coerce').notnull()]
        return clean_schedule_df

