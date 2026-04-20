import requests
import time
import csv

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,litecoin&vs_currencies=usd"

btc_target = 70000
eth_target = 4000

btc_alert_sent = False
eth_alert_sent = False

with open("Alerts.csv","a",newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Time", "coin","Price","Message"])
    
    while True:
        response = requests.get(url)
        data = response.json()
        
        bitcoin = data["bitcoin"]["usd"]
        ethereum = data["ethereum"]["usd"]
        
        
        current_time = time.ctime()
        
        print("\n--- Checking Prices---")
        
        print("Bitcoin",bitcoin)
        print("Ethereum",ethereum)
        
        message = ""
        
        if bitcoin >= btc_target and not btc_alert_sent:
            message = "Bitcoin reached target!!"
            print(message)
            btc_alert_sent = True
            
        writer.writerow([current_time,"Bitcoin",bitcoin, message])
        
        if ethereum >= eth_target and not eth_alert_sent:
            message = "Ethereum reached target"
            print(message)
            
            writer.writerow([current_time,"Ethereum",ethereum,message])
            eth_alert_sent = True
            
        time.sleep(10)