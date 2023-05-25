import requests
from bs4 import BeautifulSoup
import time

API_URL = 'https://www.binance.com/ru/futures/ETH_USDT'
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
price = None
while True:
    time.sleep(2)
    response = requests.get(API_URL, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    res = soup.find('title')
    current_price = float(res.text.split(' | ')[0])
    if price:
        new_price = ((current_price - price) / price) * 100
        if abs(new_price) >=1:
            print(f"Цена изменилась на {new_price}%")
    price = current_price
    print(price)
    time.sleep(60)





