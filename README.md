# Automatic Filmai.in Refresher

## Description

```
Generate points automatically with Automatic Filmai.in Refresher!
No longer needed to open and refresh Filmai.in page manually to receive points! Lunch this script on your server by the instructions below and enjoy!

* The page will load once every 24 hours at 5 am.

Waiting for your feedback!
```

## Start project on server

```
#GIT
git clone https://github.com/programeriss/Automatic-Filmai.in-Refresher.git

#CONFIGURATION
Edit: login.py, by the comments: 
# enter your filmai.in username here
# enter you filmai.in password here

Edit: email.php, by the comments: 
# enter email address here
# enter email address password here

composer install

#PYTHON
sudo apt-get update;
sudo apt-get install -y python
sudo apt-get update;
sudo apt-get install -y pip
sudo pip install selenium
sudo pip install selenium-wire
sudo pip install Selenium-Screenshot
composer require "swiftmailer/swiftmailer:^6.0"

#TEST
cd /var/www/html/Automatic-Filmai.in-Refresher; python3 login.py
cd /var/www/html/Automatic-Filmai.in-Refresher; php email.php

#CRONTAB
crontab -e
00 05 * * * cd /var/www/html/Automatic-Filmai.in-Refresher; python3 login.py > /dev/null 2>&1
05 05 * * * cd /var/www/html/Automatic-Filmai.in-Refresher; php email.php > /dev/null 2>&1
```

## Start project locally

```
#GIT
git clone https://github.com/programeriss/Automatic-Filmai.in-Refresher.git

#CONFIGURATION
Edit: login.py, by the comments: 
# enter your filmai.in username here
# enter you filmai.in password here

#PYTHON
sudo apt-get update;
sudo apt-get install -y python
sudo apt-get update;
sudo apt-get install -y pip
sudo pip install selenium
sudo pip install selenium-wire
sudo apt-get install wget
sudo apt-get update;
sudo apt install -y ./google-chrome*.deb

#LUNCH
Edit: login.py, by commenting this line: "chromeOptions.add_argument('--headless')" 
cd /var/www/html/Automatic-Filmai.in-Refresher; python3 login.py
```
