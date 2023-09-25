import logging
import os
from typing import Union, Any, Optional


def list_of_valid_files(directory_path: str) -> list:
    """
    This function returns a list of valid jsonl files in the directory path
    :param directory_path:
    :return:
    """
    import os
    # Declare an empty list to store the file names
    files = []
    # Looping through each file in the path
    for file in os.listdir(directory_path):
        # Checking if the file is a jsonl file
        # print(file)
        if file[-5:] == "jsonl":
            # Appending the file name to the list
            files.append(file)
    return files


def full_path_generator(directory_path: str, filepath: str) -> str:
    """
    This function returns a str of the full path of the files
    :param directory_path:
    :return:
    """
    full_path = os.path.join(directory_path, filepath)
    # Appending the full path to the list
    return full_path


full_path_generator(directory_path="data", filepath="en-US.jsonl")

from pandas import DataFrame, Series


def dataframe_gen_from_jsonl(file_path: str) -> DataFrame:
    dff = pd.read_json(file_path, lines=True)
    return dff


def en_base_df(directory_path: str) -> DataFrame:
    """
    This function returns the base dataframe for the english language
    :return:
    """
    # Getting the list of valid files
    files = list_of_valid_files(directory_path=directory_path)
    # Getting the full paths of the files
    # Checking for en-US.jsonl file in files
    if "en-US.jsonl" in files:
        # Getting the full path of the en-US.jsonl file
        en_us_path = full_path_generator(directory_path=directory_path, filepath="en-US.jsonl")
        # Generating the dataframe
        en_us_df = dataframe_gen_from_jsonl(file_path=en_us_path)
        # Renaming the columns
        en_us_df = en_us_df.rename(columns={"id": "id", "utt": "en-US_utt", "annot_utt": "en-US_annot"})
        en_us_df = en_us_df[["id", "en-US_utt", "en-US_annot"]]
        # Returning the dataframe
        return en_us_df
    else:
        raise Exception("en-US.jsonl file is not present in the directory path")


def per_language_pivot_en(directory_path: str, filepath: str) -> DataFrame:
    '''
    This function returns a dataframe where utt, annon_utt are added to the base dataframe
    for the specific passed file path
    :param directory_path:
    :param filepath:
    :return:
    '''
    # Generating english base DataFrame
    english_base_df = en_base_df(directory_path="directory_path")
    # Getting the language code from the file path
    language_code = filepath[-11:-9]
    # Getting the dataframe for the specific language
    df = dataframe_gen_from_jsonl(file_path=filepath)
    # Renaming the columns
    df = df.rename(columns={"id": "id", "utt": f"{language_code}_utt", "annot_utt": f"{language_code}_annot"})
    df = df[["id", f"{language_code}_utt", f"{language_code}_annot"]]
    # Merging the dataframes
    merged_df = pd.merge(left=english_base_df, right=df, on="id", how="left")
    # Returning the merged dataframe
    return merged_df


def excel_files_gen(input_directory_path: str, output_directory_path: str) -> list:
    """
    This function returns a list of excel files generated from the jsonl files
    :param output_directory_path:
    :param input_directory_path:
    :return:
    """
    # Declare an empty list to store the excel file names
    excel_files_paths = []
    # Looping through each file in the list of full paths
    files = list_of_valid_files(directory_path=input_directory_path)
    # remove en-US.jsonl from the list of files
    files.remove("en-US.jsonl")
    for file in files:
        language_code = file[-11:-9]
        df = per_language_pivot_en(directory_path=input_directory_path, filepath=file)
        # Output the dataframe to excel to specified output directory
        # the output name format is en-xx.xlsx where xx is the langauge code
        output_path = os.path.join(output_directory_path, f"en-{language_code}.xlsx")
        excel_files_paths.append((df,output_path))

    return excel_files_paths


def generate(output_directory_path: str, input_directory_path) -> bool:
    # Getting the list of Excel file paths
    excel_files_paths = excel_files_gen(input_directory_path=input_directory_path,
                                        output_directory_path=output_directory_path)
    # Wrap in a try-catch block
    try:
        # Looping through each file path
        for file in excel_files_paths:
            # Writing the dataframe to excel
            df = file[0]
            output_path = file[1]
            logging.info(f"Writing the dataframe to excel file: {output_path}")
            df.to_excel(output_path, index=False)
    except Exception as e:
        # Printing the error message
        print(e)
        # Returning False
        return False
