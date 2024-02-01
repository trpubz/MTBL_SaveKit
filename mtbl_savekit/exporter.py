# MTBL SaveKit - Exporter
# author: pubins.taylor
# date_modified: 2024-02-01
# version: 0.1.0
# description: reusable dataframe exporter

import os


def export_dataframe(df, filename, file_type, directory="/Users/Shared/BaseballHQ/resources/extract/", **kwargs):
    """
    Export dataframe to specified file type/location; storage to raw files -- either after or before transformations.
    :param df: pandas dataframe object
    :param filename: desired file name
    :param file_type: desired file type [should come in with '.' dot]; typically .csv or .json
    :param directory: ETL data directory
    :param kwargs: json file schema options; e.g. {schema: True, index: False}
    :return: None
    """
    # check to make sure the directory exists; if not, create it
    directory = directory
    os.makedirs(directory, exist_ok=True)
    filename = filename
    # check to make sure file_type has a '.' dot
    if not file_type.startswith("."):
        file_type = "." + file_type

    full_path = os.path.join(directory, filename + file_type)

    match file_type:
        case ".csv":
            export_to_csv(df, full_path, kwargs.get("index", False))
        case ".json":
            export_to_json(df, full_path, kwargs.get("index", False), kwargs.get("schema", True))


def export_to_csv(df, full_path, index=False):
    df.to_csv(full_path, index=index)


def export_to_json(df, full_path, index=False, with_schema=True):
    # orienting on table adds schema information to the json file
    if with_schema:
        df.to_json(full_path, index=index, orient="table", indent=2)
    else:
        df.to_json(full_path, index=index, orient="records", indent=2)
    # print("JSON file created successfully...")

