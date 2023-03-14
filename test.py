import requests
import json
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
            'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

main_url = "https://www.nseindia.com/"
response = requests.get(main_url, headers=headers)
#print(response.status_code)
cookies = response.cookies

url = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"
bank_nifty_oi_data = requests.get(url, headers=headers, cookies=cookies)
print(bank_nifty_oi_data.json())
with open(f'data.json', "w") as outfile:
    json.dump(bank_nifty_oi_data.json(), outfile)
