#!/bin/bash

# Create a virtual environment without relying on ensurepip
python3.11 -m venv venv --without-pip && \
source venv/bin/activate && \
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
python get-pip.py && \
rm get-pip.py && \
pip install --upgrade pip && \
pip install -r requirements.txt