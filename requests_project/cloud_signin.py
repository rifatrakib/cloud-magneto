import requests
from requests_project.utils import build_base_url


def login(config):
    subdomain = config.get("LOGIN_SUBDOMAIN")
    login_credentials = {
        "email": config.get("EMAIL"),
        "password": config.get("PASSWORD"),
    }
    base_url = build_base_url(config, subdomain)
    url = f"{base_url}/login"
    r = requests.post(url, data=login_credentials)
    cookies = r.cookies.get_dict()
    return cookies
