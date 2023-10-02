# Massive Dataset Project

Translation Dataset Processing Project

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)


## Introduction

The Massive Dataset Project is a Python3-based solution designed for handling and processing a massive dataset with language translations. This project is designed to provide a clear and organized solution to the assessment questions while showcasing best practices in Python development, file management, and documentation.


### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+ installed on your system.
- [Optional] A virtual environment tool like `virtualenv` or `conda`.
- Access to the MASSIVE Dataset mentioned in the Data File provided.
- Proper setup of the Python development environment, including the installation of the listed requirements from `requirements.txt`.



### Installation

Clone the Repository:

Open your terminal and navigate to the directory where you want to store the project.

Run the following command to clone the repository:

```bash
git clone https://github.com/your-username/your-project.git
```

Navigate to the Project Directory:

Change your working directory to the project folder:

```bash
cd your-project
```
Create and Activate a Virtual Environment :

To isolate your project's dependencies, you can create a virtual environment. Run these commands:

```bash
virtualenv venv
source venv/bin/activate
```
Install Dependencies:

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

These are the instructions to achieve specified goals:

#### Question 1: Generating en-xx.xlxs Files

In this question, you will generate en-xx.xlsx files for all languages based on the MASSIVE Dataset. Make sure you have set up the environment as described above.

1. **Navigate to the Project Directory**:

   Make sure you are in the project directory where the Python scripts are located.

2. **Run the Question 1 Script**:

   Execute the script for Question 1:

   ```bash
   python question1_script.py
   ```

   This script will process the dataset and generate en-xx.xlsx files for all languages where English is the pivot language.

#### Question 2: Working with Files

In this question, you will generate separate JSONL files for English (en), Swahili (sw), and German (de) for the 'test,' 'train,' and 'dev' datasets. Additionally, you'll create a large JSON file showing all translations from en to xx with 'id' and 'utt' for all train sets. You'll also pretty print the JSON structure.

1. **Run the Question 2 Script**:

   Execute the script for Question 2:

   ```bash
   python question2_script.py
   ```

   This script will generate the following:

   - Separate JSONL files for 'test,' 'train,' and 'dev' datasets for English, Swahili, and German.
   - One large JSON file containing translations from English (en) to other languages (xx) for the 'train' dataset with 'id' and 'utt.'
   - The JSON structure will be pretty printed for readability.

### Uploading Files

After running the scripts, you can upload the generated files to your Google Drive Backup Folder and all changes to your GitHub repository.

1. **Google Drive Backup Folder**:

   Manually upload the generated files to your Google Drive Backup Folder.

2. **GitHub Repository**:

   Commit and push all changes to the GitHub repository to keep your code and generated files versioned.


## Contributing

If you'd like to contribute code to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Submit a Pull Request (PR) with a clear description of your changes and why they are valuable.



