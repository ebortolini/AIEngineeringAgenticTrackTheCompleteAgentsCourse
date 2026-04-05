FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

# Remove the stale Yarn apt source from the base image so feature installs can run apt safely.
RUN rm -f /etc/apt/sources.list.d/yarn.list /usr/share/keyrings/yarn-archive-keyring.gpg
