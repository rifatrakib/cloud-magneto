from time import sleep
from utils import get_config
from requests_project.cloud_signin import login
from requests_project.scraper import scrape_data
from requests_project.utils import build_static_cookie, build_static_header
from requests_project.cloud_resources import (
    collect_cloud_record, collect_cloud_resources, collect_cloud_pages)


def initialize_crawler(headers, cookies):
    data = collect_cloud_pages(headers, cookies)
    return data["count"]


def run_crawler(headers, cookies, count):
    limiter = int(get_config("MAX_ITEM_PER_PAGE"))
    total_page = (count // limiter) + 1
    
    for page in range(1, total_page + 1):
        data = collect_cloud_resources(headers, cookies, page)
        scrape_data(data)
        sleep(int(get_config("WAITING_PERIOD")))
        break


def authenticate():
    login_cookies = login()
    cookies = build_static_cookie(get_config("STATIC_COOKIES"))
    cookies.update(login_cookies)
    headers = build_static_header(get_config("STATIC_HEADERS"))
    return cookies, headers


def start_crawler(headers, cookies):
    count = initialize_crawler(headers, cookies)
    run_crawler(headers, cookies, count)
