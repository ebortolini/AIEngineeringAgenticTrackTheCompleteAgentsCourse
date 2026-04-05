FROM node:20-bullseye-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install Python and pip, then install necessary Python packages
RUN apt-get update \
 && rm -f /etc/apt/sources.list.d/yarn.list || true \
 && apt-get -y install --no-install-recommends ca-certificates software-properties-common python3 python3-pip \
 && python3 -m pip install --upgrade pip \
 && python3 -m pip install ipykernel jupyter \
 && rm -rf /var/lib/apt/lists/*

USER root
