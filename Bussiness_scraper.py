import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=uganda"

headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
businesses = soup.find_all("div", class_="result")

print("Businesses found:", len(businesses))

with open('businesses.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Business Name', 'Phone Number', 'Address'])
    
    for business in businesses:
        name = business.find("a", class_="business-name")
        phone = business.find("div", class_="phones")
        
        if name:
            business_name = name.text.strip()
            business_phone = phone.text.strip() if phone else "N/A"
            writer.writerow([business_name, business_phone])
    print("Done! Check the businesses.csv file for the results.")