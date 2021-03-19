import requests

password_api_url = "https://api.pwnedpasswords.com/range/" + "password123"
res = requests.get(password_api_url)
print(res)