import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch email credentials from .env file
sender_email = os.getenv("sender_mail")
password = os.getenv("sender_password")
receiver_email = os.getenv("receiver_mail")

url = "https://www.libri.hu/konyv/william_buxton.grand-prix-a-forma-1-illusztralt-tortenete.html"

def scrape_data():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find("div", class_="main-col flex-grow-1 px-ms-4 px-lg-5 px-xl-64px")
    title = articles.find("h1", class_="h2 mb-2").text.strip()
    price = int(''.join(re.findall(r'\d+', articles.find("div", class_="online").text.strip())))
    return title, price

def send_email_notification(book_title, current_price, lower_bound):
    subject = f"Price Alert: {book_title} is now below {lower_bound} Ft!"
    body = f"The book '{book_title}' is now available for {current_price}, go ahead and order it!"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

def price_tracker(lower_bound):
    title, price = scrape_data()
    today = datetime.date.today()
    file_path = 'C:/Users/sogor/OneDrive/Documents/DataScientist_practice/datasets/LibriBook.xlsx'

    book_details = {"title": title, "price": price, "date": today}
    try:
        df_existing = pd.read_excel(file_path)
        df_new = pd.DataFrame([book_details])
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    except FileNotFoundError:
        df_combined = pd.DataFrame([book_details])
    df_combined.to_excel(file_path, index=False)

    if price <= lower_bound:
        send_email_notification(title, f"{price} Ft", lower_bound)

while True:
    price_tracker(8100)
    time.sleep(86400)  