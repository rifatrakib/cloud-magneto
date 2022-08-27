from requests_project.cloud_signin import login
from requests_project.cloud_resources import collect_cloud_record

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ar-AE;q=0.6,ar;q=0.5,bn-BD;q=0.4,bn;q=0.3",
    "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}


def call_scraper(config):
    login_cookies = login(config)
    print(login_cookies)
    data = collect_cloud_record(config, headers)
    print(data)
