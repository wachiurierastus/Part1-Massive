# Clone the GitHub repository
git clone https://github.com/wachiurierastus/Part1-Massive

# Change directory to the cloned repository
Set-Location -Path "Part1-Massive"

# Downloading and unzipping Massive dataset
Invoke-WebRequest -Uri "https://amazon-massive-nlu-dataset.s3.amazonaws.com/amazon-massive-dataset-1.0.tar.gz" -OutFile "amazon-massive-dataset-1.0.tar.gz"
tar -xzvf .\amazon-massive-dataset-1.0.tar.gz
Rename-Item -Path ".\amazon-massive-dataset-1.0\data" -NewName "data"

# Check if Python is installed
if (-Not (Test-Path "C:\Python38\python.exe")) {
  Write-Host "Python is not installed. Please install Python manually and rerun the script."
  Write-Host "You can download Python from https://www.python.org/downloads/"
  Exit
}

# Create a Python virtual environment
python -m venv env

# Activate the virtual environment
.\env\Scripts\Activate

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# You may need to handle the elevation of permissions manually on Windows for the generate script
# Running scripts with elevated permissions typically requires user interaction

Write-Host "Installation complete."
Write-Host "To Run the first task, run:"
Write-Host "# .\generate.ps1"
Write-Host "To Run the second task, run:"
Write-Host "# .\generate.ps1 task2"
