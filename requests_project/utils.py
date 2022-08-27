def build_base_url(config, subdomain):
    target_domain = config.get("TARGET_DOMAIN")
    protocol = config.get("PROTOCOL")
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
