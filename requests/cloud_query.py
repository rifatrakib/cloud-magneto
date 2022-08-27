import os
import requests
from hyper.contrib import HTTP20Adapter


def include_page_headers(base_url, route, headers):
    headers.update({
        ":authority": base_url.replace("https://", "")[:-1],
        ":method": "GET",
        ":path": route,
    })
    return headers


def create_http2_session(headers, url):
    session = requests.Session()
    adapter = HTTP20Adapter(headers=headers)
    session.mount(url, adapter=adapter)
    return session


def send_request(headers, api, base_url, endpoint, parameters):
    base_url = base_url.replace("https://app", f"https://{api}")
    route = f"{endpoint}/{parameters}"
    url = f"{base_url}/{route}"
    headers = include_page_headers(base_url, route, headers)
    session = create_http2_session(headers, url)
    r = session.get(url)
    data = r.json()
    return data
