FROM debian
RUN apt-get -y update
RUN apt-get -y install apache
COPY httpd.conf /usr/local/apache2/conf/
COPY index.html /usr/local/apache2/www
CMD /usr/bin/apache2ctl -D FOREGROUND
EXPOSE 8081
RUN echo "ServerName localhost" >> /usr/local/apache2/conf/apache2.conf