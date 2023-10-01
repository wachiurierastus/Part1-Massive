import TaskHelpers
from TaskHelpers import *


class TaskOne:
    def __init__(self, input_directory_path: str, output_directory_path: str):
        self.input_directory_path = input_directory_path
        self.output_directory_path = output_directory_path

    def excel_files_gen(self) -> list:
        """
        This function returns a list of Excel files generated from the jsonl files

        :return:
        """

        # Declare an empty list to store the Excel file names
        excel_files_paths = []
        # Looping through each file in the list of full paths
        files = list_of_valid_files(input_directory_path=self.input_directory_path)
        # remove en-US.jsonl from the list of files
        files.remove("en-US.jsonl")
        for file in files:
            language_code = file[-11:-9]
            df = TaskHelpers.per_language_pivot_en(filepath=file)
            # Output the dataframe to excel to specified output directory
            # the output name format is en-xx.xlsx where xx is the langauge code
            output_path = os.path.join(self.output_directory_path, f"en-{language_code}.xlsx")
            excel_files_paths.append((df, output_path))
        return excel_files_paths

    def generate(self) -> bool:
        # Getting the list of Excel file paths
        excel_files_paths = self.excel_files_gen(input_directory_path=self.input_directory_path,
                                                 output_directory_path=self.output_directory_path)
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
