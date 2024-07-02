import requests

url = "https://joeschmoe.io/api/v1/shivam"

querystring = {"eid":"1234%2F12345%2F12345","etimestamp":"11%2F11%2F2012 11%3A11%3A11","secretKey":<secretkey>,"captchaValue":"1234"}

headers = {
    'x-rapidapi-host': "aadharcardstatus.p.rapidapi.com",
    'x-rapidapi-key': <key>
    }

response = requests.request("GET", url)
for i in response:
    print(i)

# print(response.text)
