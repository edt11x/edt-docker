FROM ubuntu:20.04

RUN apt-get update
RUN apt-get upgrade -y
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -yq \
apt-file \
astyle \
autoconf \
bash \
bc \
binfmt-support \
bison \
build-essential \
ccache \
chrpath \
clang \
cmake \
cpio \
cppcheck \
curl \
debianutils \
diffstat \
dnsmasq \
dnsutils \
docker \
docker-compose \
docker-doc \
docker-registry \
docker.io \
doxygen \
ethtool \
file \
flex \
fonts-indic \
fonts-ipafont-gothic \
fonts-ipafont-mincho \
fonts-nanum \
fonts-wqy-microhei \
fonts-wqy-zenhei \
g++-9-multilib \
gawk \
gcc-9-multilib \
gdb \
git \
git-core \
glances \
gnome-tweaks \
graphviz \
gzip \
htop \
inetutils-tools \
inetutils-traceroute \
iperf3 \
iproute2 \
iputils-ping \
iwyu \
kpartx \
lib32asan5 \
lib32atomic1 \
lib32gcc-9-dev \
lib32gomp1 \
lib32itm1 \
lib32quadmath0 \
lib32stdc++-9-dev \
lib32stdc++6-9-dbg \
lib32ubsan1 \
libc-ares-dev \
libc6-dev \
libc6-dev-i386 \
libc6-dev-x32 \
libc6-x32 \
libcurl4-openssl-dev \
libegl1-mesa \
libelf-dev \
libev-dev \
libevent-dev \
liblz4-tool \
libncurses5-dev \
libpango1.0-0 \
libperl-dev \
libsdl1.2-dev \
libssl-dev \
libtool \
libu2f-udev \
libx32asan5 \
libx32atomic1 \
libx32gcc-9-dev \
libx32gcc-s1 \
libx32gomp1 \
libx32itm1 \
libx32quadmath0 \
libx32stdc++-9-dev \
libx32stdc++6 \
libx32stdc++6-9-dbg \
libx32ubsan1 \
locales \
locate \
lshw \
lsof \
lzop \
make \
meld \
minicom \
mtd-utils \
net-tools \
node-grunt-cli \
nodejs \
npm \
ntpdate \
nvme-cli \
openjdk-11-jre \
openjdk-11-jre-headless \
openjdk-8-jre-headless \
openvpn \
p7zip-full \
par2 \
pip \
procps \
putty \
python3 \
python3-dev \
python3-git \
python3-gpg \
python3-jinja2 \
python3-pexpect \
python3-pip \
python3-polib \
python3-subunit \
python3-tk \
python3-virtualenv \
qemu-system-arm \
qemu-user-static \
quilt \
ripgrep \
rsync \
ruby \
scons \
screen \
secure-delete \
socat \
sudo \
sysstat \
tcpdump \
texinfo \
tmux \
tmux-plugin-manager \
unzip \
vim \
vim-gtk3 \
wget \
xsltproc \
xterm \
xz-utils \
zlib1g \
zlib1g-dev \
&& apt-get clean

ENV PYTHONDONTWRITEBYTECODE 1
ENV PHYTHONUNBUFFERED 1

RUN pip install wic
RUN pip install kas

RUN sudo locale-gen en_US.UTF-8
RUN groupadd -g 1000 user
RUN useradd -m -u 1000 -g 1000 user
RUN echo "user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/usersudo
RUN chmod 400 /etc/sudoers.d/usersudo
USER user

CMD ["/bin/bash"]
