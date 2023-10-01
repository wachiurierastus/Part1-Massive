import logging

import pandas as pd
from pandas import DataFrame
import FileParsing
import functions
from FileParsing import *


class TaskTwo:
    # initialize the class
    def __init__(self, input_directory_path: str, output_directory_path: str):
        self.input_directory_path = input_directory_path
        self.output_directory_path = output_directory_path
        self.parser = FileParsing(input_directory_path=input_directory_path,
                                  output_directory_path=output_directory_path)

    @staticmethod
    def partition(df: DataFrame, part: str) -> DataFrame:
        part = part.lower()
        if part == "train" or part == "dev" or part == "test":
            df = df[df["partition"] == part]
            return df
        else:
            raise Exception("Invalid partition")

    def partitions_gen(self, df: DataFrame) -> list:
        parts = ["train", "dev", "test"]
        partitions = []
        for part in parts:
            dff = self.partition(df=df, part=part)
            partitions.append(dff)
        return partitions

    def task22(self, output_directory_path: str, input_directory_path: str, languages: list) -> None:
        files = self.parser.list_of_valid_files(directory_path=input_directory_path)
        # Check directories exist
        if (self.parser.directory_checker(directory_path=input_directory_path, purpose="input") and
                self.parser.directory_checker(directory_path=output_directory_path, purpose="output")):
            supported_langs = []
            counter = 0
            # language generating function.
            for file in files:
                language_code = file[-11:-9]
                supported_langs.append(language_code)
                # print(files)
            print(supported_langs)
            for file in files:
                for i in range(len(languages)):
                    counter = counter + 1
                    if languages[i] in supported_langs:
                        file_path = full_path_generator(directory_path=input_directory_path, filepath=file)
                        print(file_path)
                        dff = dataframe_gen_from_jsonl(file_path=file_path)
                        partitions = self.partitions_gen(df=dff)
                        for j in range(len(partitions)):
                            partition_name = ""
                            if j == 0:
                                partition_name = "train"
                            elif j == 1:
                                partition_name = "dev"
                            else:
                                partition_name = "test"

                            out_dir_path = os.path.join(output_directory_path, f"{partition_name}")
                            os.makedirs(out_dir_path, exist_ok=True)
                            # print(out_dir_path)
                            output_path = full_path_generator(out_dir_path,
                                                                          f"{languages[i]}-1{partition_name}.jsonl")
                            print(output_path)
                            self.parser.save_to_jsonl(df=partitions[j], output_path=output_path)
                            print(counter)
                    else:
                        raise Exception("Invalid language code")
                break

        else:
            raise Exception("Invalid directory path")

    def task23(self, lang_input_directory: str, input_directory: str) -> json:

        # check if the directory name ends in train

        if lang_input_directory[-5:] == 'train':
            df_list = []
            print('yes')
            files = self.parser.list_of_valid_files(directory_path=lang_input_directory)
            # print(files)
            for file in files:
                # print(file)
                language_code = file[-11:-9]
                print(language_code)
                df = dataframe_gen_from_jsonl(full_path_generator(directory_path=
                                                                                          lang_input_directory, filepath=file))
                new_df = self.parser.per_language_pivot_en(lang_directory_path=lang_input_directory, filepath=file,
                                                           input_directory_path=input_directory)
                df_list.append(new_df)
                # print(df_list)
            # return pd.concat(df_list)
        else:
            raise Exception("Invalid directory")
