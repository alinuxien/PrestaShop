FROM prestashop/prestashop-git:latest

RUN (adduser --system --uid=$(id -u $USER) --gid=$(id -g $USER) \
        --home /home/jenkins --shell /bin/bash jenkins)

# To run files with the same group as your primary user
RUN groupmod -g $(id -g $USER) www-data \
  && usermod -u $(id -u $USER) -g $(id -g $USER) www-data

COPY /wait-for-it.sh /tmp/
COPY /docker_run_git.sh /tmp/

RUN mkdir -p /var/www/.npm
RUN chown -R www-data:www-data /var/www/.npm

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install -y nodejs

CMD ["/tmp/docker_run_git.sh"]
