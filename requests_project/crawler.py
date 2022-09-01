from time import sleep
from utils import get_config
from requests_project.scraper import scrape_data
from requests_project.cloud_auth import authenticate
from requests_project.cloud_records import record_endpoints
from requests_project.cloud_resources import collect_cloud_resources, collect_cloud_pages


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
        record = record_endpoints(data[4:])
        # sleep(int(get_config("WAITING_PERIOD")))
        break


def start_crawler():
    count = initialize_crawler()
    run_crawler(count)
