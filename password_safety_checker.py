import requests
import hashlib
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
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')

def pwned_api_check(password):
    # check if our password in the returned list
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password

# request_api_data('123')
print(pwned_api_check('123'))