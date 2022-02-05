FROM bitnami/minideb:latest
RUN apt install git nginx php php-fpm php-curl -y
# INSTALL WHAT WE Need
COPY / .
#
#
#EXPOSING SOME PORTS
EXPOSE 80 443
#
#
# ENTRYPOINT
