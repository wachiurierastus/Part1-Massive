import argparse
import TaskHelpers
import TaskOne
import TaskTwo


def main():
    parser = argparse.ArgumentParser(description="Command-line argument example")
    parser.add_argument('--task', required=True, help="The task to perform")
    parser.add_argument('-i', '--input', required=True, help="Input directory")
    parser.add_argument('-o', '--output', required=True, help="Output directory")

    args = parser.parse_args()

    # Your code to perform the specified task goes here
    if args.task == "task1":
        task_one = TaskOne.TaskOne(input_directory_path=args.input, output_directory_path=args.output)
        task_one.generate()
    elif args.task == "task2":
        task_two = TaskTwo.TaskTwo(input_directory_path=args.input, output_directory_path=args.output)
        task_two.task22(input_directory_path=args.input, output_directory_path=args.output, languages=["en", "es"])
        task_two.task22(input_directory_path=args.input, output_directory_path=args.output, languages=["en", "es"])
    else:
        print("Invalid task")


if __name__ == "__main__":
    main()
