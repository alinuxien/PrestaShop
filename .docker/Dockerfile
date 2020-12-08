FROM prestashop/prestashop-git:latest

RUN addgroup --system --gid eval$(id -g $USER ) jenkins \
 && adduser --system --uid eval$(id -u $USER ) -ingroup jenkins \
        --home /home/jenkins --shell /bin/bash jenkins    

# To run files with the same group as your primary user
RUN groupmod -g jenkins www-data \
  && usermod -u jenkins -g jenkins www-data

COPY /wait-for-it.sh /tmp/
COPY /docker_run_git.sh /tmp/

RUN mkdir -p /var/www/.npm
RUN chown -R www-data:www-data /var/www/.npm

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install -y nodejs

CMD ["/tmp/docker_run_git.sh"]
