#!/bin/bash

# Clone the GitHub repository
git clone https://github.com/wachiurierastus/Part1-Massive

# Change directory to the cloned repository
cd Part1-Massive || exit


# Downloading and unzipping Massive dataset
curl https://amazon-massive-nlu-dataset.s3.amazonaws.com/amazon-massive-dataset-1.0.tar.gz --output amazon-massive-dataset-1.0.tar.gz
tar -xzvf amazon-massive-dataset-1.0.tar.gz
mv amazon-massive-dataset-1.0/data data
# Check if python is installed
if ! command -v python &>/dev/null; then
  echo "Python is not installed. Installing Python..."
  sudo apt-get update
  sudo apt-get install python3.8
fi

# Create a Python virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Elevate the generate shell
echo "Needs admin, Enter sudo password below:"
sudo chmod +x generate.sh
mkdir /outputs

echo "Installation complete."

echo "To Run the first task, run: "

echo" # ./generate.sh"
echo"To Run the second task, run:"

echo "# ./generate.sh task2"

