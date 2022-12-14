import requests
from hyper.contrib import HTTP20Adapter
from requests_project.cloud_auth import authenticate
from requests_project.utils import get_headers_and_cookies


def include_page_headers(base_url, route, headers, http_method, protocol):
    headers.update({
        ":scheme": protocol,
        "referer": f"{base_url}/",
        "origin": base_url,
        ":authority": base_url.replace("https://", ""),
        ":method": http_method,
        ":path": f"/{route}",
    })
    return headers


def create_http2_session(headers, url):
    session = requests.Session()
    adapter = HTTP20Adapter(headers=headers)
    session.mount(url, adapter=adapter)
    return session


def send_request(base_url, endpoint, http_method, protocol, parameters=None, data=None):
    headers, cookies = get_headers_and_cookies()
    if parameters:
        if parameters.startswith("?"):
            route = f"{endpoint}{parameters}"
        else:
            route = f"{endpoint}/{parameters}"
    else:
        route = endpoint
    
    url = f"{base_url}/{route}"
    print(f"{url=}\t{data=}")
    headers = include_page_headers(base_url, route, headers, http_method, protocol)
    session = create_http2_session(headers, url)
    method = getattr(session, http_method.lower())
    
    r = method(url, cookies=cookies, json=data)
    
    if r.status_code == 200:
        data = r.json()
        
        if isinstance(data, dict):
            if "error" in data and data["error"] == "Not logged in":
                print(data)
                _ = authenticate()
                data = send_request(
                    base_url, endpoint, http_method, protocol, parameters, data)
    else:
        data = None
    
    return data
