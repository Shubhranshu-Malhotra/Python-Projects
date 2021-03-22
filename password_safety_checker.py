import requests

password_api_url = "https://api.pwnedpasswords.com/range/" + "password123"
res = requests.get(password_api_url)
print(res)

password_api_url = "https://api.pwnedpasswords.com/range/" + "CBFDA"   # starting letters of hashcode
res = requests.get(password_api_url)
print(res)

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError('Error fetching: {}')

def pwned_api_check(password):
    pass