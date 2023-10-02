import json
import os
import logging
from pandas import DataFrame
import pandas as pd
from typing import *
from TaskHelpers import *


def dataframe_gen_from_jsonl(file_path: str) -> DataFrame:
    try:
        df = pd.read_json(file_path, orient='records', lines=True)
        return df
    except Exception as e:
        print(e)
        print(" " + "Something went wrong reading file" + f" {file_path}")
        return pd.DataFrame()


def df_to_excel(df: DataFrame, output_path: str) -> bool:
    """
        This function returns a bool of whether the dataframe was successfully saved to excel
        :param df:
        :param output_path:
        :return:
        """
    try:
        if df.empty:
            raise Exception("Dataframe is empty")
        else:
            df.to_excel(output_path, index=False)
            return True
    except Exception as e:
        print(e)
        raise Exception("Error saving to excel")


def directory_checker(directory_path: str, purpose: str) -> bool:
    """
    This function checks if the directory path exists
    :param purpose:
    :param use:
    :param directory_path:
    :return:
    """
    # Check if directory exists, if it doesn't check its use, if use is output, create the directory in the parent of
    # input directory.
    if os.path.isdir(directory_path):
        return True
    else:
        if purpose == "output":
            # Create the directory
            os.mkdir(directory_path)
            return True
        else:
            raise Exception("Invalid directory path")


def full_path_generator(directory_path: str, filepath: str) -> str:
    """
    This function returns a str of the full path of the files
    :param filepath:
    :param directory_path:
    :return:
    """
    full_path = os.path.join(directory_path, filepath)
    # Appending the full path to the list
    return full_path


def list_of_valid_files(input_directory_path: str) -> list:
    """
        This function returns a list of valid jsonl files in the directory path
        :param input_directory_path:
        :param self:
        :return:
        """
    import os
    # Declare an empty list to store the file names
    files = []
    # Looping through each file in the path
    for file in os.listdir(input_directory_path):
        # Checking if the file is a jsonl file
        # print(file)
        if file[-5:] == "jsonl":
            # Appending the file name to the list
            files.append(file)
    return files


def save_to_jsonl(df: DataFrame, output_path: str, lines: bool) -> bool:
    try:
        if df.empty:
            raise Exception("Dataframe is empty")
        else:
            df.to_json(output_path, orient="records", lines=lines)
            return True
    except Exception as e:
        print(e)
        raise Exception("Error saving to jsonl")
