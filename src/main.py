import argparse
import TaskOne
import TaskTwo
from dotenv import load_dotenv
import os


def main():
    parser = argparse.ArgumentParser(description="Command-line argument example")
    parser.add_argument('--task', required=True, help="The task to perform")
    parser.add_argument('-i', '--input', required=True, help="Input directory")
    parser.add_argument('-o', '--output', required=True, help="Output directory")
    #Add optional argument Save
    parser.add_argument("-s", "--save",required=False, help="Save to google drive")

    args = parser.parse_args()
    # Your code to perform the specified task goes here
    if args.task == "task1":
        task_one = TaskOne.TaskOne(input_directory_path=args.input, output_directory_path=args.output)
        task_one.generate()
    elif args.task == "task2":
        task_two = TaskTwo.TaskTwo(input_directory_path=args.input, output_directory_path=args.output)
        task_two.task22(input_directory_path=args.input, output_directory_path=args.output, languages=["en", "es"])
        print(task_two.task23())
    else:
        print("Invalid task")


if __name__ == "__main__":
    main()
