
FROM ubuntu:22.04

RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y \
bash \
bridge-utils \
busybox \
coreutils \
iproute2 \
iputils-ping \
openssh-client \
net-tools && \
apt-get clean

RUN mkdir -p /root/.ssh && chmod 700 /root/.ssh
COPY id_rsa.pub /root/.ssh/authorized_keys
RUN chown root:root /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

CMD ["/bin/bash"]

