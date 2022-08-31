from utils import get_config


def build_base_url(subdomain):
    target_domain = get_config("TARGET_DOMAIN")
    protocol = get_config("PROTOCOL")
    return f"{protocol}://{subdomain}.{target_domain}"


def build_static_cookie(cookie_string):
    cookies = {}
    for cookie in cookie_string.split("; "):
        key, value = cookie.split("=", 1)
        cookies[key] = value
    
    return cookies


def build_static_header(header_string):
    headers = {}
    for header in header_string.split("|"):
        key, value = header.split("=", 1)
        headers[key] = value
    
    return headers


def get_headers_and_cookies():
    cookies = build_static_cookie(get_config("STATIC_COOKIES"))
    headers = build_static_header(get_config("STATIC_HEADERS"))
    
    login_cookies = get_config("login_cookies")
    if login_cookies:
        cookies.update(login_cookies)
    
    return headers, cookies
