
FROM alpine:latest

RUN apk add --update --no-cache \
  bash

COPY docker-init /etc/

CMD ["/etc/docker-init"]


