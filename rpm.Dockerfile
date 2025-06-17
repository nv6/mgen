# syntax=docker/dockerfile:1.16-labs

FROM almalinux:9.5 AS builder

RUN dnf update --refresh \
  && dnf install git epel-release dnf-plugins-core -y \
  && dnf config-manager --set-enabled crb \
  && dnf group install -y "Development Tools" \
  && dnf install libpcap-devel rpmdevtools rpmlint -y

WORKDIR /root

RUN git clone https://github.com/nv6/mgen.git

WORKDIR mgen

RUN git submodule update --init

RUN rpmdev-setuptree && rpmbuild -ba mgen.spec

######

FROM scratch AS exporter

COPY --from=builder --parents /root/rpmbuild/./* .