import requests
url = "https://api.github.com"
response = requests.get(url)
data = response.json()
print(data["current_user_url"])