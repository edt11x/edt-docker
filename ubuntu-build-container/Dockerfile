FROM arm64v8/ubuntu:20.04

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -yq \
bash \
astyle \
bridge-utils \
build-essential \
busybox \
chrpath \
coreutils \
cpio \
debianutils \
diffstat \
doxygen \
htop \
g++ \
gawk \
gcc \
gdb \
git-core \
graphviz \
gzip \
iproute2 \
iputils-ping \
kpartx \
libelf-dev \
libsdl1.2-dev \
lzop \
mtd-utils \
nodejs \
node-grunt-cli \
npm \
openvpn \
pip \
python3-dev \
python3-virtualenv \
python3 \
python3-pexpect \
python3-pip \
quilt \
ripgrep \
ruby \
scons \
secure-delete \
socat \
tcpdump \
texinfo \
unzip \
wget \
xclip \
xterm \
xz-utils \
par2 \
procps \
curl \
file \
git \
zlib1g \
zlib1g-dev \
vim-gtk3 \
vim \
clang \
quilt \
autoconf \
libtool \
libevent-dev \
ntpdate \
screen \
meld \
gnome-tweaks \
cppcheck \
iwyu \
locate \
ethtool \
iperf3 \
htop \
glances \
p7zip-full \
net-tools && \
apt-get clean

RUN groupadd -g 1000 user
RUN useradd -m -u 1000 -g 1000 user
USER user

CMD ["/bin/bash"]
