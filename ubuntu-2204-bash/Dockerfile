
FROM ubuntu:22.04

RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y \
bash \
bridge-utils \
coreutils \
iproute2 \
iputils-ping \
net-tools && \
apt-get clean

CMD ["/bin/bash"]

