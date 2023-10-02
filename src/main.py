import argparse
import TaskOne
import TaskTwo
from dotenv import load_dotenv
import os
import google_drive_save


def main():
    parser = argparse.ArgumentParser(description="Command-line argument example")
    parser.add_argument('--task', required=True, help="The task to perform")
    parser.add_argument('-i', '--input', required=True, help="Input directory")
    parser.add_argument('-o', '--output', required=True, help="Output directory")
    # Add optional argument Save
    parser.add_argument("-s", "--save", required=False, help="Save to google drive")

    args = parser.parse_args()
    # Your code to perform the specified task goes here
    if args.task == "task1":
        task_one = TaskOne.TaskOne(input_directory_path=args.input, output_directory_path=args.output)
        task_one.generate()
    elif args.task == "task2":
        task_two = TaskTwo.TaskTwo(input_directory_path=args.input, output_directory_path=args.output)
        task_two.task22(input_directory_path=args.input, output_directory_path=args.output,
                        languages=["en", "de", "sw"])
        print(task_two.task23())
    elif args.task == "save":
        # Save to google Drive
        google_drive_save.upload_to_gdrive(source_directory=args.output, destination_folder_name="output",
                                           parent_folder_name="cat1")
    else:
        print("Invalid task")


''''
    # Save to google drive
    if args.save:
        load_dotenv()
        google_drive_save.upload_to_gdrive(source_directory=args.output, destination_folder_name="output",
                                           parent_folder_name="cat1")
        print("Saved to google drive")
'''

if __name__ == "__main__":
    main()
