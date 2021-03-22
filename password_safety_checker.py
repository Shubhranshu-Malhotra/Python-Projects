import requests

password_api_url = "https://api.pwnedpasswords.com/range/" + "password123"
res = requests.get(password_api_url)
print(res)

password_api_url = "https://api.pwnedpasswords.com/range/" + "CBFDA"   # starting letters of hashcode
res = requests.get(password_api_url)
print(res)

def request_api_data(query_char):
    pass

def pwned_api_check(password):
    pass