#web Scraping Project
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv

#Connect to website
url = 'https://realpython.github.io/fake-jobs/'

#Create BeautifulSoup object
page = requests.get(url)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

#Data to be obtained: Job title, Company, Location, Date posted
job_title, company, location, date_posted = [],[],[],[]
def get_data():
    for i in soup2.find_all('h2'):
        job_title.append(i.string.strip())

    for i in soup2.find_all('h3'):
        company.append(i.string.strip())

    for i in soup2.find_all(class_="location"):
        location.append(i.string.strip())

    for i in soup2.find_all('time'):
        date_posted.append(i.string.strip())
    
    print("Data Retrieval Successful")

#Calling function to get data and insert into appropriate lists
get_data()

#Headers to be used in the csv file
headers = ['Job Title','Company','Location','Date Posted']

#Creating csv and adding header data
with open('Python Jobs.csv','w',newline='',encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)

#Appending scraped data into csv
with open('Python Jobs.csv','a+',newline='',encoding='UTF-8') as f:
    for i in range(len(job_title)):
        data = [job_title[i],company[i],location[i],date_posted[i]]
        writer = csv.writer(f)
        writer.writerow(data)

print("File creation and Data Insertion Successful!")

