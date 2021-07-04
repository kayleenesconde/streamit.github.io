import csv
import pandas as pd
from logging import exception
from os import link
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
print("")
print (driver.title)
Categories = []
Categories.append(["TOPIC","DESCRIPTION", "OTHER CATEGORIES","LAST EDITED","COPYRIGHT"])

val = input("Search: ")
print("")
print("Scraping...")
print("")

search = driver.find_element_by_name("search")
search.send_keys(val)
search.send_keys(Keys.RETURN)

link = driver.find_element_by_class_name("searchmatch")
link.click()
element_present = EC.presence_of_element_located((By.ID, 'bodyContent'))

try:
    
    title= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'firstHeading'))
    )
    description = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="mw-parser-output"]/p[2]'))
    )
    categ = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'catlinks'))
    )
    ToU = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'footer-info-copyright'))
    )
    last = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "footer-info-lastmod"))
    )
    print("---TOPIC---")
    print (title.text)
    print("")
    print("---DESCRIPTION---")
    print (description.text)
    print("")
    print("---OTHER CATEGORIES---")
    print (categ.text)
    print("")
    print("---COPYRIGHT---")
    print (ToU.text)
    print("")
    print("---LAST EDITED---")
    print (last.text)
    Categories.append([title.text,description.text,categ.text,last.text,ToU.text])
except:
    print ('The topic does not yet exist on Wikipedia.')
    driver.close()

with open(val+'.csv', 'w', encoding='utf-8') as file:
    Import = csv.writer(file, lineterminator='\n')
    Import.writerows(Categories)
from prettytable import PrettyTable 
  
# open csv file 
#a = open(val+".csv", 'r') 
  
# read the csv file 
#a = a.readlines() 
  
# Seperating the Headers 
#l1 = a[0] 
#l1 = l1.split(',') 
  
# headers for table 
#t = PrettyTable([l1[0], l1[1]]) 
  
# Adding the data 
#for i in range(1, len(a)) : 
    #t.add_row(a[i].split(',')) 
  
#code = t.get_html_string() 
#html_file = open("output.html", 'w') 
#html_file = html_file.write(code)