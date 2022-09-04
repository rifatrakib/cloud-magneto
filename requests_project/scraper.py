import numpy as np
import pandas as pd
from utils import get_config
from toolz.dicttoolz import keyfilter


def get_matching_columns(columns, suffix):
    columns = columns.to_list()
    matches = [col for col in columns if col.endswith(f"_{suffix}")]
    return matches


def make_non_negative(data):
    result = data.where(data >= 0, -data)
    return result


def convert_to_datetime(data):
    result = pd.to_datetime(data, errors="coerce")
    return result


def extract_wanted_fields(data):
    unwanted = {"city_label", "postal_code_label", "postal_region"}
    filterer = lambda key: key not in unwanted
    result = list(map(lambda doc: keyfilter(filterer, doc), data))
    return result


def scrape_data(data):
    data = extract_wanted_fields(data)
    link_field = get_config("RECORD_LINK_FIELD")
    
    dtypes = {}
    for item in get_config("RESOUCE_DTYPES").split(","):
        key, value = item.split("=")
        dtypes[key] = value
    
    df = pd.DataFrame(data)
    df["sections"] = pd.to_numeric(df["sections"], errors="coerce")
    df = df.astype(dtypes)
    
    date_columns = get_matching_columns(df.columns, "date")
    df[date_columns] = df[date_columns].apply(convert_to_datetime)
    
    numeric_columns = df.select_dtypes(include=np.number).columns
    df[numeric_columns] = df[numeric_columns].apply(make_non_negative)
    
    string_columns = [col for col, dtype in dtypes.items() if dtype == "str" and not col.endswith("_date")]
    df[string_columns] = df[string_columns].apply(lambda x: x.str.lower())
    
    df["record_link_short"] = df[link_field].str.rsplit("-", 2).str.get(0)
    df["record_link_full"] = df[link_field]
    
    df = df.replace({np.nan: None, pd.NA: None})
    data = df.to_dict(orient="records")
    
    return data
