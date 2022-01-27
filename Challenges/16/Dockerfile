FROM debian
RUN apt-get install httpd
COPY httpd.conf /usr/local/apache2/conf/
COPY index.html /usr/local/apache2/www
CMD [“/usr/sbin/httpd”, “-D”, “FOREGROUND”]
RUN a2enmod rewrite
EXPOSE 8081