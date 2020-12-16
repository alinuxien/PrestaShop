FROM prestashop/prestashop-git:latest

# To run files with the same group as your primary user
RUN groupmod -g 1000 www-data \
  && usermod -u 1000 -g 1000 www-data

COPY /wait-for-it.sh /tmp/
COPY /docker_run_git.sh /tmp/

RUN mkdir -p /var/www/.npm
RUN chown -R www-data:www-data /var/www/.npm

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install -y nodejs

COPY . /var/www/html
RUN chown -R www-data:www-data /var/www/html

WORKDIR /var/www/html

ENV COMPOSER_MEMORY_LIMIT=4G

RUN runuser -g www-data -u www-data -- /usr/local/bin/composer install --no-interaction
RUN runuser -g www-data -u www-data -- /usr/bin/make assets

CMD ["/tmp/docker_run_git.sh"]
