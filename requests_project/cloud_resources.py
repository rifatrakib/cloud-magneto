from utils import get_config
from requests_project.utils import build_base_url
from requests_project.cloud_store import store_data
from requests_project.cloud_query import send_request


def read_subdomain_env(section):
    subdomain = get_config(f"{section}_SUBDOMAIN")
    http_method = get_config(f"{section}_METHOD")
    endpoint = get_config(f"{section}_ENDPOINT")
    protocol = get_config("PROTOCOL")
    
    return subdomain, http_method, endpoint, protocol


def collect_cloud_pages():
    subdomain, http_method, endpoint, protocol = read_subdomain_env("COUNTER")
    base_url = build_base_url(subdomain)
    payload = {"default": True, "cacheable": True}
    data = send_request(base_url, endpoint, http_method, protocol, data=payload)
    return data


def collect_cloud_resources(page):
    subdomain, http_method, endpoint, protocol = read_subdomain_env("RESOURCE")
    base_url = build_base_url(subdomain)
    payload = {"page": page}
    data = send_request(base_url, endpoint, http_method, protocol, data=payload)
    return data


def collect_cloud_record(section, parameter_data=None, payload=None):
    parameters = None
    
    subdomain, http_method, endpoint, protocol = read_subdomain_env(section)
    base_url = build_base_url(subdomain)
    parameter_fields = get_config(f"{section}_PARAM")
    
    if parameter_fields:
        parameter_fields = parameter_fields.split(",")
        parameter_list = [f"{field}={value}" for field, value in zip(parameter_fields, [parameter_data])]
        parameters = "&".join(parameter_list)
        parameters = f"?{parameters}"
    elif parameter_data:
        parameters = f"{parameter_data}"
    
    data = send_request(
        base_url, endpoint, http_method, protocol,
        parameters=parameters, data=payload)
    
    return data
