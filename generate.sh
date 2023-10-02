#!/bin/bash

task="$1"
cd src || exit
case "$task" in
  task1)
    python -m main --task task1 --input "../data" --output "../outputs"
    ;;
  task2)
    python -m main --task task2 --input "../data" --output "../outputs"
    ;;
  *)
    echo "Invalid task: $task. Use 'task1' or 'task2'."
    exit 1
    ;;
esac






