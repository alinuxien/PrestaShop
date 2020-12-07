FROM prestashop/prestashop-git:latest

RUN (adduser --system --uid=114 --gid=120 \
        --home /home/jenkins --shell /bin/bash jenkins)

# To run files with the same group as your primary user
RUN groupmod -g 120 www-data \
  && usermod -u 114 -g 120 www-data

COPY /wait-for-it.sh /tmp/
COPY /docker_run_git.sh /tmp/

RUN mkdir -p /var/www/.npm
RUN chown -R www-data:www-data /var/www/.npm

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt install -y nodejs

CMD ["/tmp/docker_run_git.sh"]
