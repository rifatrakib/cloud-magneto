import os
from dotenv import load_dotenv
from cloud_signin import login
from cloud_query import send_request

load_dotenv()
base_url = os.environ.get("SITE_URL")

credentials = {
    "email": os.environ.get("EMAIL"),
    "password": os.environ.get("PASSWORD"),
}

headers = {
    "referer": f"{base_url}/",
    ":scheme": "https",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ar-AE;q=0.6,ar;q=0.5,bn-BD;q=0.4,bn;q=0.3",
    "origin": base_url,
    "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}


if __name__ == '__main__':
    login_cookies = login(base_url, credentials)
    info_subdomain = os.environ.get("INFO_SUBDOMAIN")
    info_endpoint = os.environ.get("INFO_ENDPOINT")
    query_parameter = os.environ.get("PARAM")
    data = send_request(
        headers, info_subdomain, base_url,
        info_endpoint, query_parameter)
    print(data)
