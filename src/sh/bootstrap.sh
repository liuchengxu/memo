#!/usr/bin/env bash

set -e

apt-get update && apt-get upgrade -y

DEBIAN_FRONTEND=noninteractive apt-get install python-software-properties software-properties-common -y
LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php -y
apt-get update

# Install php7.2
DEBIAN_FRONTEND=noninteractive apt-get install -y git vim php7.2 php-mongodb php-pear php7.2-curl php7.2-dev php7.2-gd php7.2-mbstring php7.2-zip php7.2-mysql php7.2-xml

# Install mongodb
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y mongodb-org --allow-unauthenticated

# Install composer
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install apcu and mongodb extension via pecl
printf "\n" | pecl -d php_suffix=7.2 install apcu
echo "extension = apcu.so" | tee -a /etc/php/7.2/mods-available/apcu.ini
pecl -d php_suffix=7.2 install mongodb
echo "extension = mongodb.so" | tee -a /etc/php/7.2/mods-available/mongodb.ini

# Install Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
apt-get update
apt-get install -y docker-ce

# Install nodejs
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
apt-get update && apt-get install yarn

# Install angular via yarn
yarn global bin
yarn global add @angular/cli

git clone https://github.com/EOSEssentials/EOSTracker-API --depth=1 && cd EOSTracker-API
composer require symfony/requirements-checker
composer install
