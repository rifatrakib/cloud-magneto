import requests
from hyper.contrib import HTTP20Adapter


def include_page_headers(base_url, route, headers, http_method, protocol):
    headers.update({
        ":scheme": protocol,
        "referer": f"{base_url}/",
        "origin": base_url,
        ":authority": base_url.replace("https://", "")[:-1],
        ":method": http_method,
        ":path": route,
    })
    return headers


def create_http2_session(headers, url):
    session = requests.Session()
    adapter = HTTP20Adapter(headers=headers)
    session.mount(url, adapter=adapter)
    return session


def send_request(headers, base_url, endpoint, parameters, http_method, protocol):
    route = f"{endpoint}/{parameters}"
    url = f"{base_url}/{route}"
    headers = include_page_headers(base_url, route, headers, http_method, protocol)
    session = create_http2_session(headers, url)
    method = getattr(session, http_method.lower())
    r = method(url)
    data = r.json()
    return data
