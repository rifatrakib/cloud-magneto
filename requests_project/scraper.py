from requests_project.cloud_signin import login
from requests_project.cloud_resources import collect_cloud_record, collect_cloud_resources

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

cookies = {
    '_hjSessionUser_2746983': 'eyJpZCI6IjY2YzY2YjQzLWQ4NTktNWMwMy1iZGRlLTFmYjliMzM0MGUzNiIsImNyZWF0ZWQiOjE2Mzk3MTYxOTYxMDMsImV4aXN0aW5nIjp0cnVlfQ==',
    '_ga': 'GA1.2.402241433.1639716195',
    '_ga_0K3KJ2JHN7': 'GS1.1.1645529148.42.1.1645529434.0',
    '_hp2_ses_props.1771820804': '{"ts":1661600995021,"d":"app.propcloud.no","h":"/","g":"#/"}',
    '_hp2_id.1771820804': '%7B%22userId%22%3A%223547709716783584%22%2C%22pageviewId%22%3A%223411401215319534%22%2C%22sessionId%22%3A%223103760310917442%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D'
}


def call_scraper(config):
    login_cookies = login(config)
    cookies.update(login_cookies)
    print(cookies)
    data = collect_cloud_record(config, headers)
    print(data)
    print(collect_cloud_resources(config, headers, cookies))
