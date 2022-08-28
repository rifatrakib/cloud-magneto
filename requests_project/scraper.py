import numpy as np
import pandas as pd
from toolz.dicttoolz import keyfilter


def get_matching_columns(columns, suffix):
    columns = columns.to_list()
    matches = [col for col in columns if col.endswith(f"_{suffix}")]
    return matches


def make_non_negative(data):
    result = data.clip(0, data.max())
    return result


def extract_wanted_fields(data):
    unwanted = {"city_label", "postal_code_label", "postal_region"}
    filterer = lambda key: key not in unwanted
    result = list(map(lambda doc: keyfilter(filterer, doc), data))
    return result


def scrape_data(data):
    data = extract_wanted_fields(data)
    dtypes = {
        'address': 'str', 'addresses': 'Int64', 'area': 'float64',
        'arealbruk': 'float64', 'bathrooms': 'Int64', 'buildings': 'Int64',
        'built_area': 'float64', 'byggeaar': 'float64', 'bygningskategori': 'float64',
        'city_name': 'str', 'city_number': 'Int64', 'county_name': 'str',
        'county_number': 'Int64', 'energikarakter': 'float64', 'geometry': 'object',
        'gnr': 'Int64', 'house_number': 'float64', 'industry_code': 'str',
        'industry_code_name': 'str', 'lat': 'float64', 'leases': 'Int64',
        'lnr': 'Int64', 'lon': 'float64', 'oppvarmingskarakter': 'float64',
        'plots': 'Int64', 'postal_code': 'Int64', 'postal_location': 'str',
        'property_id': 'Int64', 'property_id_nma': 'str', 'property_type_name': 'str',
        'purchase_price': 'float64', 'reguleringsformål': 'float64', 'rooms': 'float64',
        'sections': 'Int64', 'snr': 'Int64', 'street_name': 'str',
        'transaction_date': 'str', 'type': 'str', 'ufs_home': 'float64',
        'ufs_other': 'float64', 'ufs_total': 'float64', 'unr': 'Int64',
        'utilization': 'float64', 'utstedelsesdato': 'float64', 'wcs': 'float64'
    }
    
    df = pd.DataFrame(data)
    df["sections"] = pd.to_numeric(df["sections"], errors="coerce")
    df = df.astype(dtypes)
    
    date_columns = get_matching_columns(df.columns, "date")
    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")
    
    numeric_columns = df.select_dtypes(include=np.number).columns
    string_columns = filter(lambda x: x == "str", dtypes)
    df[numeric_columns] = df[numeric_columns].apply(make_non_negative)
    df[string_columns] = df[string_columns].apply(str.lower)
    
    data = df.to_dict(orient="records")
    return data
