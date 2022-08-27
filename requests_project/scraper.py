from requests_project.cloud_signin import login
from requests_project.utils import build_static_cookie, build_static_header
from requests_project.cloud_resources import (
    collect_cloud_record, collect_cloud_resources, collect_cloud_pages)


def call_scraper(config):
    login_cookies = login(config)
    cookies = build_static_cookie(config["STATIC_COOKIES"])
    cookies.update(login_cookies)
    headers = build_static_header(config["STATIC_HEADERS"])
    count_data = collect_cloud_pages(config, headers, cookies)
    print(count_data)
    resource_data = collect_cloud_resources(config, headers, cookies)
    print(resource_data)
