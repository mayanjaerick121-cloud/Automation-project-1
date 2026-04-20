import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.upwork.com/jobs?q=python&l=remote"
headers = {"user-agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
jobs = soup.find_all("div", class_="job_seen_beacon")
print("Jobs found:", len(jobs))

with open('remote_jobs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Company', 'Location', 'Summary'])
    
    for job in jobs:
        title = job.find("h2", class_="jobTitle")
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        summary = job.find("div", class_="job-snippet")
        
        if title and company and location and summary:
            job_title = title.text.strip()
            company_name = company.text.strip()
            job_location = location.text.strip()
            job_summary = summary.text.strip().replace('\n', ' ')
            writer.writerow([job_title, company_name, job_location, job_summary])
    print("Done! Check the remote_jobs.csv file for the results.")