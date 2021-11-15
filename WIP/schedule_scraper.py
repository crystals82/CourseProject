from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import re 
import urllib
import time
import pandas as pd
import lxml
import html5lib

options = Options()
options.headless = True
driver = webdriver.Chrome('/Users/adam/Downloads/chromedriver',options=options)

def get_js_soup(url,driver):
    driver.get(url)
    res_html = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(res_html,'html.parser') #beautiful soup object to be used for parsing html content
    return soup

sup = get_js_soup('https://www.icccricketschedule.com/icc-cricket-t20-world-cup-2021-schedule-team-venue-time-table-pdf-point-table-ranking-winning-prediction/',driver)
j13 = sup.find_all(class_ = 'wp-block-table is-style-stripes')
mytables = sup.find_all("table")
new_list = []
cur_list = []

for i in range(0,len(mytables)):
    var = (mytables[i].findAll(text='Match No'))
    if len(var) > 0:
        
        df = pd.read_html(str(mytables[i]))
        new_list.append(df[0])

for j in range(0,len(new_list)):
    
    try:
        cur_var = str(j13[j].previousSibling.previousSibling.text.encode('ascii', 'ignore').decode('ascii'))
    except :
        cur_var = str(j13[j].previousSibling.previousSibling.previousSibling.text.encode('ascii', 'ignore').decode('ascii'))
    
    cur_var = cur_var.replace(":","").replace(" Fixture","")
    
    var_split = cur_var.split()
    if len(var_split) > 2:
        group_num = var_split[3]
        round_type = var_split[0] + ' ' + var_split[1]
    else :
        group_num = ''
        round_type = var_split[0] + ' ' + var_split[1]
    cur_list.append(cur_var)
    new_list[j]['round_type'] = round_type
    new_list[j]['group_num'] = group_num

    col_list = []
    for u in list(new_list[j].columns.values):
        clean_u = u.replace(' ','_').lower()
        col_list.append(clean_u)

    new_list[j].columns = col_list
    new_list[j]['team_1'] = new_list[j]['match_centers'].str.split(' Vs ').str[0]
    new_list[j]['team_2'] = new_list[j]['match_centers'].str.split(' Vs ').str[1]
    new_list[j]['clean_datetime_of_match_ist'] = pd.to_datetime(new_list[j]['date'] + ' ' + new_list[j]['time'])
    new_list[j]['clean_datetime_of_match_ist'] = new_list[j]['clean_datetime_of_match_ist'].dt.tz_localize('Asia/Kolkata')
    new_list[j]['clean_datetime_of_match_est'] = new_list[j]['clean_datetime_of_match_ist'].dt.tz_convert('America/New_York')

final_clean_df = pd.concat(new_list,ignore_index = True) 
final_clean_df.to_csv('cricket_t20_world_cup.csv', encoding='utf-8')