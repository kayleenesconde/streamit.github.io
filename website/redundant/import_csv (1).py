import csv
from logging import exception
from time import sleep
from os import link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.justwatch.com")
print("")
print (driver.title)
Categories = []
Categories.append(["TITLE","PICTURE", "LOCATION"])

val = input("Search: ")
print("")
print("Scraping...")
print("")

search = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/div/ion-searchbar/div/input')
search.send_keys(val)
sleep(5)
search.click()
sleep(1)
search.send_keys(Keys.RETURN)

try:
    
    title= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="base"]/div[3]/div/div/div[2]/ion-grid/div/ion-row[1]/ion-col[2]/a/span[1]'))
    )
    description = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="base"]/div[3]/div/div/div[2]/ion-grid/div/ion-row[1]/ion-col[1]/a/div'))
    )
    categ = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="base"]/div[3]/div/div/div[2]/ion-grid/div/ion-row[1]/ion-col[2]/div[1]/div/div/div[1]/div[2]/div/div/a/img'))
    )

    print("---TOPIC---")
    print (title.text)
    print("")
    print("---DESCRIPTION---")
    print (description.text)
    print("")
    print("---LOCATION---")
    print (categ.text)
    print("")
    Categories.append([title.text,description.text,categ.text,last.text,ToU.text])
except:
    print ('The topic does not yet exist on Wikipedia.')
    driver.close()

with open(val+'.csv', 'w', encoding='utf-8') as file:
    Import = csv.writer(file, lineterminator='\n')
    Import.writerows(Categories)