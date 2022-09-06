from pymongo import MongoClient
from utils import get_config


class MongoConnectionManager():
    def __init__(self, collection):
        self.client = MongoClient(get_config("MONGO_URI"))
        self.database = get_config("DATABASE_NAME")
        self.collection = collection
    
    def __enter__(self):
        self.database = self.client[self.database]
        self.collection = self.database[self.collection]
        return self.collection
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()


def build_base_url(subdomain):
    target_domain = get_config("TARGET_DOMAIN")
    protocol = get_config("PROTOCOL")
    return f"{protocol}://{subdomain}.{target_domain}"


def build_static_cookie(cookie_string):
    cookies = {}
    for cookie in cookie_string.split("; "):
        key, value = cookie.split("=", 1)
        cookies[key] = value
    
    return cookies


def build_static_header(header_string):
    headers = {}
    for header in header_string.split("|"):
        key, value = header.split("=", 1)
        headers[key] = value
    
    return headers


def get_headers_and_cookies():
    cookies = build_static_cookie(get_config("STATIC_COOKIES"))
    headers = build_static_header(get_config("STATIC_HEADERS"))
    
    login_cookies = get_config("login_cookies")
    if login_cookies:
        cookies.update(login_cookies)
    
    return headers, cookies
