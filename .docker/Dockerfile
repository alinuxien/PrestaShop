FROM prestashop/prestashop-git:latest

# To run files with the same group as your primary user
RUN groupmod -g 1000 www-data \
  && usermod -u 1000 -g 1000 www-data

RUN mkdir -p /var/www/.npm
RUN chown -R www-data:www-data /var/www/.npm

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install -y nodejs

COPY . /var/www/html

WORKDIR /var/www/html

ENV COMPOSER_MEMORY_LIMIT=4G
RUN composer update --no-dev --prefer-dist || true

RUN APP_ENV=prod APP_DEBUG=0 php bin/console cache:clear
