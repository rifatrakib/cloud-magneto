from requests_project.utils import build_base_url
from requests_project.cloud_query import send_request


def read_subdomain_env(config, section):
    subdomain = config.get(f"{section}_SUBDOMAIN")
    http_method = config.get(f"{section}_METHOD")
    endpoint = config.get(f"{section}_ENDPOINT")
    protocol = config.get("PROTOCOL")
    
    return subdomain, http_method, endpoint, protocol


def collect_cloud_resources(config, headers, login_cookies):
    subdomain, http_method, endpoint, protocol = read_subdomain_env(config, "RESOURCE")
    base_url = build_base_url(config, subdomain)
    payload = {"page": 1, "cacheable": True}
    data = send_request(headers, base_url, endpoint, http_method, protocol, cookies=login_cookies, data=payload)
    return data


def collect_cloud_record(config, headers):
    subdomain, http_method, endpoint, protocol = read_subdomain_env(config, "INFO")
    base_url = build_base_url(config, subdomain)
    parameters = config.get("PARAM")
    data = send_request(headers, base_url, endpoint, http_method, protocol, parameters=parameters)
    return data
