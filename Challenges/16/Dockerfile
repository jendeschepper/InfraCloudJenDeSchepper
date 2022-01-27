FROM httpd
COPY httpd.conf /usr/local/apache2/conf/
COPY index.html /usr/local/apache2/www
CMD httpd -D FOREGROUND
EXPOSE 8081
RUN echo "ServerName localhost" >> /usr/local/apache2/conf/apache2.conf