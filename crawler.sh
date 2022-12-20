#!/bin/bash

#for Ubuntu
pip install scrapy
pip install mysql-connector-python
sudo apt install mariadb-server
sudo apt install gcc
sudo apt install python3-dev
sudo apt install libmariadb3 libmariadb-dev
pip install mysql-connector-python

sudo yum scrapy

#for Fedora
python -m pip install scrapy
python -m pip install mysql.connector
sudo dnf install community-mysql-server -y
sudo dnf install gcc

python3 /home/chambers/Git/crawler/capstonescraper/capstonescraper/spiders/crawler.py "$@"
