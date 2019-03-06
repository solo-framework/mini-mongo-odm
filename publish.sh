#!/bin/bash

python3 -m venv .env && \
source ./.env/bin/activate && \
pip3 install -r ./requirements.txt && \
pip3 install twine && \
python setup.py sdist -v && \
twine upload dist/*