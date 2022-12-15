#!/bin/bash

pip install scrapy
pip install mysql-connector-python
sudo apt install mariadb-server
sudo apt install gcc
sudo apt install python3-dev
sudo apt install libmariadb3 libmariadb-dev


python3 /home/chambers/Git/crawler/capstonescraper/capstonescraper/spiders/crawler.py "$@"
