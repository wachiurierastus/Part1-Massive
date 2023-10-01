import json
import os
import logging
from pandas import DataFrame
from typing import *
from TaskHelpers import *


def dataframe_gen_from_jsonl(file_path: str) -> DataFrame:
    df_dictionary: Dict[str, List[Any]] = {}
    # read the file contents line by line
    try:
        with open(file_path, "r") as file_input:
            for line in file_input.readlines():
                # convert it to a python dictionary
                json_load = json.loads(line)
                for (key, value) in json_load.items():
                    if key not in df_dictionary:
                        df_dictionary[key] = []
                    df_dictionary[key].append(value)
        df = pd.DataFrame(df_dictionary)
        logging.info(f"Dataframe generated from {file_path}")
        return df
    except Exception as e:
        print(e)
        print(" " + "Something went wrong reading file" + f" {file_path}")


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


def list_of_valid_files(input_directory_path) -> list:
    """
        This function returns a list of valid jsonl files in the directory path
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
