import FileParsing
from FileParsing import *
import pandas as pd


class TaskHelpers:
    def __init__(self, input_directory_path: str, output_directory_path: str) -> object:
        self.input_directory_path = input_directory_path
        self.output_directory_path = output_directory_path

    def en_base_df(self) -> DataFrame:
        """
        This function returns the base dataframe for the english language
        :return:
        """
        # Getting the list of valid files
        files = FileParsing.list_of_valid_files(input_directory_path=self.input_directory_path)
        # Getting the full paths of the files
        # Checking for en-US.jsonl file in files
        if "en-US.jsonl" in files:
            # Getting the full path of the en-US.jsonl file
            en_us_path = FileParsing.full_path_generator(directory_path=self.input_directory_path,
                                                         filepath="../en-US.jsonl")
            # print(en_us_path)
            # Generating the dataframe
            en_us_df = FileParsing.dataframe_gen_from_jsonl(file_path=en_us_path)
            # Renaming the columns
            en_us_df = en_us_df.rename(columns={"id": "id", "utt": "en-US_utt", "annot_utt": "en-US_annot"})
            # print(en_us_df)
            en_us_df = en_us_df[["id", "en-US_utt", "en-US_annot"]]
            # Returning the dataframe
            return en_us_df
        else:
            raise Exception("en-US.jsonl file is not present in the directory path")

    def per_language_pivot_en(self, filepath: str) -> DataFrame:
        """
        This function returns a dataframe where utt, annon_utt are added to the base dataframe
        for the specific passed file path
        :param filepath:
        :return:
        """

        # Generating english base DataFrame
        print("Hi" + str(self.input_directory_path))
        english_base_df = en_base_df(input_directory_path=self.input_directory_path)
        # Getting the language code from the file path
        language_code = filepath[-11:-9]
        print(filepath)
        # Getting the dataframe for the specific language
        file_path = FileParsing.full_path_generator(directory_path=self.input_directory_path, filepath=filepath)
        df = FileParsing.dataframe_gen_from_jsonl(file_path=file_path)
        # Renaming the columns
        df = df.rename(columns={"id": "id", "utt": f"{language_code}_utt", "annot_utt": f"{language_code}_annot"})
        df = df[["id", f"{language_code}_utt", f"{language_code}_annot"]]
        # Merging the dataframes
        merged_df = pd.merge(left=english_base_df, right=df, on="id", how="left")
        # Returning the merged dataframe
        return merged_df

    def language_pivot_en(self, lang_directory_path: str, filepath: str) -> DataFrame:
        '''
        This function returns a dataframe where utt, annon_utt are added to the base dataframe
        for the specific passed file path
        :param lang_directory_path:
        :param input_directory_path:
        :param filepath:
        :return:
        '''
        # Generating english base DataFrame
        english_base_df = en_base_df(input_directory_path=self.input_directory_path)
        # Getting the language code from the file path
        language_code = filepath[-11:-9]
        print(filepath)
        # Getting the dataframe for the specific language
        df = FileParsing.dataframe_gen_from_jsonl(
            file_path=FileParsing.full_path_generator(directory_path=lang_directory_path, filepath=filepath))
        # Renaming the columns
        df = df.rename(columns={"id": "id", "utt": f"{language_code}_utt", "annot_utt": f"{language_code}_annot"})
        df = df[["id", f"{language_code}_utt", f"{language_code}_annot"]]
        # reset index
        df.reset_index(drop=True, inplace=True)
        # drop id column
        df.drop(columns=["id"], inplace=True)
        # Merging the dataframes
        merged_df = pd.concat([english_base_df, df], axis=1)
        # Returning the merged dataframe
        return merged_df
