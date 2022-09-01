from requests_project.cloud_auth import authenticate
from requests_project.crawler import start_crawler


_ = authenticate()
start_crawler()
