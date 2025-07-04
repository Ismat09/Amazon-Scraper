importing libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import time

import smtplib # for sending emails to myself
# Connect to website

URL = "https://www.amazon.ca/Sony-WH-1000XM5-Cancelling-Headphones-Hands-Free/dp/B09XSDMT4F?th=1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36", "Priority": "u=0, i"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
title = soup2.find(id="productTitle").get_text().strip()
price = soup2.find('span',class_="aok-offscreen").get_text().strip()[1:]

print(title)
print(price)
Sony WH-1000XM5 Wireless Industry Leading Noise Cancelling Headphones with Auto Noise Cancelling Optimizer, Crystal Clear Hands-Free Calling, and Alexa Voice Control, Silver
498.00
today = datetime.date.today()
print(today)
2025-05-22
import csv

header = ['Product Name', 'Price', 'Date']
data = [title,price, today]

# This code is for saving the file and data, Only Run it once
# Running it more than once will reset the data

# with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f: # w means write, newline makes it no space in between
#    writer = csv.writer(f)
#    writer.writerow(header)
#    writer.writerow(data)
# This is for appending new data

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f: # a+ for append
    writer = csv.writer(f)
    writer.writerow(data)
# Setting up send_mail function for sending an email to myself

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login('rafsanahmed.cloud@gmail.com','vwzi qbmg fzkx kcpj')

    subject = "HUGE SALE! 40% OFF & MORE! SONY XM5 IS THE CHEAPEST EVER YOU'LL FIND ON THE MARKET!"
    body = "The price has dropped significantly and now it's time to swipe! Click on the link below to start the process of emptying your wallet: https://www.amazon.ca/Sony-WH-1000XM5-Cancelling-Headphones-Hands-Free/dp/B09XSDMT4F?th=1"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('rafsanahmed.cloud@gmail.com', 'rafsangooner@gmail.com', msg)
# This the function for checking the price when price drops below a certain level

def check_price():
    URL = "https://www.amazon.ca/Sony-WH-1000XM5-Cancelling-Headphones-Hands-Free/dp/B09XSDMT4F?th=1"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36", "Priority": "u=0, i"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id="productTitle").get_text().strip()

    price = soup2.find('span',class_="aok-offscreen").get_text().strip()[1:]

    today = datetime.date.today()

    header = ['Product Name', 'Price', 'Date']

    data = [title,price, today]

    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f: # a+ for append
        writer = csv.writer(f)
        writer.writerow(data)

    if(float(price) < 298):
        send_mail()
while(True):
    check_price()
    time.sleep(86400)
df = pd.read_csv(r"C:\Users\rafsa\AmazonWebScraperDataset.csv")
# IMPORTANT! Saving the File to CSV is not necessary to get an email alert
# Saving the file is done just to store data, this code is usually run on a server

# END
