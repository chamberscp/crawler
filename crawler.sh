#!/bin/bash

pip install scrapy
pip install mysql-connector-python
sudo apt install mariadb-server

python3 /home/chambers/Git/crawler/capstonescraper/capstonescraper/spiders/crawler.py "$@"
