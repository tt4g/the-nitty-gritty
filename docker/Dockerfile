FROM debian:bullseye-20230320

RUN apt-get update \
    && apt-get install -y gcc-10=10.2.1-6 g++-10=10.2.1-6 build-essential=12.9 \
        cmake=3.18.4-2+deb11u1 \
        libspdlog-dev=1:1.8.1+ds-2.1 \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
