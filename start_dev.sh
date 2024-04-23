#!/bin/bash

# Activating the virtual environment
current_directory=$(pwd)
source $current_directory/.venv/bin/activate

uvicorn main:app --reload --port 3000