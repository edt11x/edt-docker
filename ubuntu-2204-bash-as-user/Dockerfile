
FROM ubuntu:22.04

RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y \
bash \
bridge-utils \
busybox \
coreutils \
iproute2 \
iputils-ping \
net-tools && \
apt-get clean

RUN groupadd -g 1000 user
RUN useradd -m -u 1000 -g 1000 user
USER user

CMD ["/bin/bash"]

