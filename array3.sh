#!/bin/bash

PROGRID=$(dirname "$0")
cd "${PROGRID}" || exit
source ./venv/bin/activate
python main.py
deactivate