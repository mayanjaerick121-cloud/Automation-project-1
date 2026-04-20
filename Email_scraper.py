import requests
from bs4 import BeautifulSoup
import re
import csv
url = "http://www.betika.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

text = soup.get_text()
emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)

emails = list(set(emails))
with open ("emails.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Email'])
    for email in emails:
        writer.writerow([email])
    print("Emails saved")