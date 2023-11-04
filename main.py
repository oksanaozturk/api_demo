import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=RUB&amount=10"

payload = {}
headers= {
  "apikey": "UyjuYfUUwisIrbEveW50fYYFPWnWdKG0"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)

import requests

url = "https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"

payload = {}
headers= {
  "apikey": "UyjuYfUUwisIrbEveW50fYYFPWnWdKG0"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)
