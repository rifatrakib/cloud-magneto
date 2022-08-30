from requests_project.crawler import authenticate, start_crawler


cookies, headers = authenticate()
start_crawler(headers, cookies)
