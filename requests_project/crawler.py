from time import sleep
from requests_project.cloud_signin import login
from requests_project.scraper import scrape_data
from requests_project.utils import build_static_cookie, build_static_header
from requests_project.cloud_resources import (
    collect_cloud_record, collect_cloud_resources, collect_cloud_pages)


def initialize_crawler(config, headers, cookies):
    data = collect_cloud_pages(config, headers, cookies)
    return data["count"]


def run_crawler(config, headers, cookies, count):
    limiter = int(config.get("MAX_ITEM_PER_PAGE"))
    total_page = (count // limiter) + 1
    
    for page in range(1, total_page + 1):
        data = collect_cloud_resources(config, headers, cookies, page)
        scrape_data(data)
        sleep(int(config.get("WAITING_PERIOD")))


def warm_up(config):
    login_cookies = login(config)
    cookies = build_static_cookie(config["STATIC_COOKIES"])
    cookies.update(login_cookies)
    headers = build_static_header(config["STATIC_HEADERS"])
    return cookies, headers


def start_crawler(config, headers, cookies):
    count = initialize_crawler(config, headers, cookies)
    run_crawler(config, headers, cookies, count)
