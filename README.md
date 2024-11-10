# 📚 Formula-1 Book Price Tracker 📚

As a huge fan of both reading and Formula-1, I’ve been on the lookout for a good deal on the book Grand Prix: A Forma-1 illusztrált története. To help me keep track of this book on Libri.hu, I wrote a price-tracking program that checks the price daily and sends me an email alert if it drops below my threshold. 📉 Here’s a breakdown of the project:

🛠 Technologies Used:
I used Python’s requests and BeautifulSoup libraries for data scraping, and pandas to save this data to an Excel spreadsheet. For email functionality, I used the smtplib library.

💾 Data Handling & Storage:
Each day, the program stores updated price and date information in an Excel file, so I have a complete record of price changes over time.

📧 Email Notification:
The send_email_notification function automates the alert system by comparing the current price against my target threshold. Once the price drops below my desired level, I receive an instant email to take action!

🔒 Security with .env File:
To keep my email credentials secure, I stored them in a .env file and used Python’s dotenv library to load them into the code. This ensures sensitive data is protected and keeps my code clean and secure.

Here’s a screenshot of my inbox (of course, with my email address blurred for safety).
![Formula-1 Book Tracker](/e_mail_notification.jpg)
