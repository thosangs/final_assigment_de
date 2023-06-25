from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook

from datetime import datetime
import pandas as pd
import requests
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

### defaulr args
args = {
    'owner': 'arif',
    'depends_on_past': False,
}

###funtions
#get resoinse and push it in xcom
def scrape(ti) :
    
    #load chromedrive
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    remote_webdriver = 'remote_chromedriver'
    with webdriver.Remote(f'{remote_webdriver}:4444/wd/hub',options=chrome_options) as driver:
        driver.get('https://www.youtube.com/')
        #response=driver.find_element(By.CSS_SELECTOR,'.central-textlogo__image').text
        response=driver.current_url
        pass
    ti.xcom_push(key='scrape_result',value=response)
    print('succes')


###dag tasks
with DAG(dag_id="TEST_SCRAPING",
         start_date=datetime(2023,6,24),
         catchup=False) as dag:
                
        #task to load data to mysql 
        task = PythonOperator(
        task_id="scrape",
        python_callable=scrape)


#task dependencies
task