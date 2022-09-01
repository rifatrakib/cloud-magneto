import copy
from utils import get_config
from requests_project.cloud_resources import collect_cloud_record


def unpack_query_data(section, records, accessor):
    segments = accessor.split(".")
    multi_value = get_config(f"{section}_MULTIPLE")
    
    query_value = copy.deepcopy(records)
    for segment in segments:
        if not segment:
            continue
        
        if isinstance(query_value, list):
            items = []
            for record in query_value:
                if isinstance(record, list):
                    for doc in record:
                        items.append(doc[segment])
                else:
                    items.append(record[segment])
            query_value = copy.deepcopy(items)
        else:
            query_value = query_value[segment]
    
    query_value = [str(item) for item in query_value]
    
    if multi_value:
        query_value = "%2c".join(query_value)
    
    return query_value


def prepare_query_data(section, record):
    partial = get_config(f"{section}_PARTIAL")
    trailing = get_config(f"{section}_TRAILING")
    field_name = get_config(f"{section}_QUERY_FIELD")
    print(section)
    
    if "." in field_name:
        query_value = unpack_query_data(section, record, field_name)
    else:
        query_value = record[field_name]
        query_value = query_value.rsplit("-", 2)[0] + "-0-0"
        if partial:
            query_value = query_value.rsplit("-", int(partial))[0]
        if trailing:
            query_value = query_value.lstrip("0")
    
    return query_value


def prepare_payload_data(section, record):
    payload = None
    field_name = get_config(f"{section}_PAYLOAD")
    if field_name:
        knr, gnr, bnr, _, _ = record[field_name].split("-")
        payload = {"knr": knr, "gnr": gnr, "bnr": bnr}
        print(payload)
    
    return payload


def record_endpoints(records):
    endpoints = get_config("RECORD_PAGE_ENDPOINTS").split(",")
    dependent_endpoints = {}
    for endpoint in endpoints:
        source = get_config(f"{endpoint}_SOURCE")
        if source:
            dependent_endpoints[endpoint] = source
    
    independent_endpoints = set(endpoints) - set(dependent_endpoints.keys())
    
    for record in records:
        data = {}
        for endpoint in independent_endpoints:
            query_parameters = prepare_query_data(endpoint, record)
            payload = prepare_payload_data(endpoint, record)
            
            query_parameters = None if payload else query_parameters
            
            data[endpoint] = collect_cloud_record(
                endpoint, payload=payload,
                parameter_data=query_parameters)
        
        for endpoint, source in dependent_endpoints.items():
            if not data[source]:
                continue
            
            query_parameters = prepare_query_data(endpoint, data[source])
            payload = prepare_payload_data(endpoint, data[source])
            
            query_parameters = None if payload else query_parameters
            print(f"{query_parameters=}")
            if isinstance(query_parameters, list):
                data[endpoint] = {}
                for q in query_parameters:
                    data[endpoint][q] = collect_cloud_record(endpoint, payload=payload, parameter_data=q)
            else:
                data[endpoint] = collect_cloud_record(
                    endpoint, payload=payload,
                    parameter_data=query_parameters)
        break
    
    return data
