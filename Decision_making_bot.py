import requests
import time

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,litecoin&vs_currencies=usd"

buy_price = 30000
sell_price = 70000

while True:
    response = requests.get(url)
    data = response.json()
    
    bitcoin = data["bitcoin"]["usd"]
    print("\nBitcoin:", bitcoin)
    
    if bitcoin <= buy_price:
        print("Buying signal")
    
    with open("signals.txt", "a") as file:
        file.write(f"Buy at {bitcoin} at {time.ctime()}\n")
        
        
    if bitcoin >= sell_price:
     print("Selling signal")
        
    with open("signals.txt", "a") as file:
            file.write(f"Sell at {bitcoin} at {time.ctime()}\n")
            
else:
    print("Hold")
    
time.sleep(10)