import requests


def login(base_url, login_credentials):
    url = f"{base_url}/login"
    r = requests.post(url, data=login_credentials)
    cookies = r.cookies.get_dict()
    return cookies
