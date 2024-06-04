import requests

url = "https://joeschmoe.io/api/v1/shivam"

querystring = {"eid":"1234%2F12345%2F12345","etimestamp":"11%2F11%2F2012 11%3A11%3A11","secretKey":"OBdz4sIn5fN9vgmrjaPU3wZ%2BO0mX9ndJNWCfM%2FjzeaAmc1qLSzaP7KfM4vnKJp44V0pbhajzOL2M82jJO%2FwwPmZetFO9vdsk8XJkOX7%2FfMHyoTI00FYbfdOJluk5UlNK","captchaValue":"1234"}

headers = {
    'x-rapidapi-host': "aadharcardstatus.p.rapidapi.com",
    'x-rapidapi-key': "3af9d30ea9msh32e3cfdb7df1452p16af0ejsn9cb33927a52c"
    }

response = requests.request("GET", url)
for i in response:
    print(i)

# print(response.text)