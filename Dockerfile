# Use the official Ubuntu 22.04 base image
FROM ubuntu:22.04

# Install Python 3 and pip3
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Download and install Z3 version 4.12.1.0
RUN pip install z3-solver==4.12.1.0

# Set the working directory
WORKDIR /gensys

# Copy GenSys-LTL code to the container
COPY . /gensys