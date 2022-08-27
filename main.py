from dotenv import dotenv_values
from requests_project.crawler import warm_up, start_crawler

config = dotenv_values(".env")


cookies, headers = warm_up(config)
start_crawler(config, headers, cookies)
