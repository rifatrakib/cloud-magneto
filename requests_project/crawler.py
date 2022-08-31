import requests
from time import sleep
from utils import get_config, set_config
from requests_project.scraper import scrape_data
from requests_project.utils import build_base_url
from requests_project.cloud_resources import (
    collect_cloud_record, collect_cloud_resources, collect_cloud_pages)


def initialize_crawler():
    data = collect_cloud_pages()
    
    if "error" in data:
        print(data)
        _ = authenticate()
        data = collect_cloud_pages()
    
    return data["count"]


def run_crawler(count):
    limiter = int(get_config("MAX_ITEM_PER_PAGE"))
    total_page = (count // limiter) + 1
    
    for page in range(1, total_page + 1):
        data = collect_cloud_resources(page)
        
        if "error" in data:
            print(data)
            _ = authenticate()
            data = collect_cloud_resources(page)
        
        scrape_data(data)
        sleep(int(get_config("WAITING_PERIOD")))


def authenticate():
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


def start_crawler():
    count = initialize_crawler()
    run_crawler(count)
