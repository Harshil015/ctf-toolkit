FROM kalilinux/kali-rolling

# Avoid interactive prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive

# Install core tools
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    nmap \
    ffuf \
    sqlmap \
    gdb \
    binutils \
    file \
    git \
    vim \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies globally
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --break-system-packages -r /tmp/requirements.txt

# Clone SecLists for web fuzzing (optional, can be large)
# RUN git clone --depth 1 https://github.com/danielmiessler/SecLists.git /opt/seclists

WORKDIR /ctf
