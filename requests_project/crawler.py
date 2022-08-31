from time import sleep
from utils import get_config
from requests_project.cloud_signin import login
from requests_project.scraper import scrape_data
from requests_project.cloud_resources import (
    collect_cloud_record, collect_cloud_resources, collect_cloud_pages)


def initialize_crawler():
    data = collect_cloud_pages()
    
    if "error" in data:
        print(data)
        count = authenticate(callback=initialize_crawler)
        return count
    
    return data["count"]


def run_crawler(count):
    limiter = int(get_config("MAX_ITEM_PER_PAGE"))
    total_page = (count // limiter) + 1
    
    for page in range(1, total_page + 1):
        data = collect_cloud_resources(page)
        scrape_data(data)
        sleep(int(get_config("WAITING_PERIOD")))


def authenticate(callback=None):
    login()
    if callback:
        return callback()


def start_crawler():
    count = initialize_crawler()
    run_crawler(count)
