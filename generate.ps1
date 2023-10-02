$task = $args[0]

# Change directory to 'src' or exit if it doesn't exist
Set-Location -Path ".\src" -ErrorAction Stop

switch ($task) {
    "task1" {
        python -m main --task task1 --input "..\data" --output "..\outputs"
    }
    "task2" {
        python -m main --task task2 --input "..\data" --output "..\outputs"
    }
    Default {
        Write-Host "Invalid task: $task. Use 'task1' or 'task2'."
        Exit 1
    }
}
