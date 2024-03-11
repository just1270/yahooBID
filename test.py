import requests
from bs4 import BeautifulSoup

def fetch_yahoo_auction_items():
    url = 'https://tw.bid.yahoo.com/tw'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('li', class_='BaseGridItem__grid___2wuJ7')
        
        for item in items:
            name = item.find('span', class_='BaseGridItem__title___2HWui').text
            price = item.find('em', class_='BaseGridItem__price___31jkj').text
            
            print("商品名称:", name)
            print("价格:", price)
            print("-" * 50)
    else:
        print("Failed to fetch data from Yahoo Auction")

if __name__ == "__main__":
    fetch_yahoo_auction_items()
