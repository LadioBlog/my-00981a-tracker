Python




import requests
import json
from datetime import datetime

def fetch_00981a():
    # 使用 Yahoo 財經公開的 API 節點
    url = "https://query1.finance.yahoo.com/v8/finance/chart/00981A.TW"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # 抓取最新的價格
        meta = data['chart']['result'][0]['meta']
        current_price = meta['regularMarketPrice']
        
        # 準備要存入 json 的內容
        output = {
            "price": current_price,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # 儲存成 data.json
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=4)
        print("00981A 價格更新成功！")
        
    except Exception as e:
        print(f"抓取失敗，錯誤原因: {e}")

if __name__ == "__main__":
    fetch_00981a()
