import requests 
import time


url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,litecoin&vs_currencies=usd"
  
btc_target = 70000


while True:
   response = requests.get(url)
   data = response.json()
   
   bitcoin_price = data["bitcoin"]["usd"]
   print("Bitcoin:", bitcoin_price)
   
   if bitcoin_price >= btc_target:
        print("Bitcoin has reached the target price of $70,000!")
        
        with open("alerts.txt","a") as file:
            file.write(f"Alert: Bitcoin reached ${bitcoin_price} at {time.ctime()}\n")
        break
time.sleep(10)