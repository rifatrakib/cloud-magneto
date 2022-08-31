import requests
from utils import get_config, set_config
from requests_project.utils import build_base_url


def login():
    subdomain = get_config("LOGIN_SUBDOMAIN")
    login_credentials = {
        "email": get_config("EMAIL"),
        "password": get_config("PASSWORD"),
    }
    base_url = build_base_url(subdomain)
    url = f"{base_url}/login"
    print(f"{url=}")
    
    r = requests.post(url, data=login_credentials)
    cookies = r.cookies.get_dict()
    set_config("login_cookies", cookies)
