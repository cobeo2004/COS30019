#!/bin/bash

# Check if at least one argument is provided
if [ -z "$1" ]; then
  echo "No argument provided. Usage: sh run.sh [test|main] [additional arguments...]"
  exit 1
fi

# Get the first argument
command=$1
shift

# Run the corresponding Python script based on the first argument and pass the remaining arguments
case $command in
  test)
    python Tests/main.py "$@"
    ;;
  main)
    python iengine.py "$@"
    ;;
    reference)
    python References/InferenceEngine-master/InferenceEngine.py "$@"
    ;;
    genHF)
    python Components/Datasets/CreateHornTestCases.py "$@"
    ;;
  *)
    echo "Invalid argument. Usage: sh run.sh [test|main] [additional arguments...]"
    exit 1
    ;;
esac
