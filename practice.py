from email.policy import default
import pandas as pd
import numpy as np
import csv


# url이 있는 열까지만 표기.

df = pd.read_csv('add_store_score.csv', encoding='cp949')
columns = ['store_address', 'store_score']
df.drop(columns, axis=1, inplace= True)

# 셀레니움
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



#기본값
default_comment = ''

comment_house = []

chromedriver = r'C:\Users\j.park\practice\selenium_practice\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)


for i, url in enumerate(df['naver_store_url']):
    
    driver.get(url +'/review/visitor')
    time.sleep(1)
    
    try:
        search_review = driver.find_elements(by=By.CLASS_NAME, value= "WoYOw")
        for comment in search_review:
            x = comment.get_attribute('innerText')
            default_comment = default_comment +'/' + x  
        comment_house.append(default_comment)
        default_comment = ''

        
    except Exception as e1 :
        print(f'{i}행에 리뷰가 존재하지 않음')
    
        ax = 'Null'
        comment_house.append(ax)    
     

driver.quit()

df['visitor_review'] = comment_house
df_comment = df['visitor_review']
df.to_csv('c:/Users/j.park/practice/selenium_practice/sample_comment.csv',index = False, encoding='utf-8')
