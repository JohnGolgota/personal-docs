FROM php:8.2.4-apache

WORKDIR /var/www/html

ADD --chmod=0755 https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/

RUN a2enmod rewrite

RUN a2enmod headers

RUN apt-get update && apt-get install -y unzip git

COPY --from=composer /usr/bin/composer /usr/local/bin/composer

RUN install-php-extensions pdo_mysql mysqli mbstring gd xdebug
