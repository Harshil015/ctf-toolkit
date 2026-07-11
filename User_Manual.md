# CTF Automation Toolkit - User Manual

Welcome to the **CTF Automation Toolkit**! This manual will guide you through installing, configuring, and using the toolkit to accelerate your CTF, bug bounty, and vulnerability disclosure workflows.

---

## Table of Contents
1. [Introduction](#1-introduction)
2. [Installation](#2-installation)
   - [Option A: Local Installation](#option-a-local-installation-recommended)
   - [Option B: Docker Environment](#option-b-docker-environment)
3. [Command Structure](#3-command-structure)
4. [Module Usage & Examples](#4-module-usage--examples)
   - [Web Module](#web-module)
   - [Pwn Module](#pwn-module)
   - [Crypto Module](#crypto-module)
   - [Reverse Engineering Module](#reverse-engineering-module)
5. [Infrastructure & Docker Usage](#5-infrastructure--docker-usage)
6. [Extending the Toolkit](#6-extending-the-toolkit)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. Introduction
The CTF Automation Toolkit is a modular command-line interface (CLI) tool designed to eliminate repetitive tasks during security competitions and bug bounty hunting. Instead of writing custom Python scripts for every new challenge, this toolkit provides pre-built templates for web exploitation, binary pwn, cryptography, and reverse engineering, all unified under a single `ctf-toolkit` command.

---

## 2. Installation

### Option A: Local Installation (Recommended)
Installing locally adds the `ctf-toolkit` command to your system PATH, allowing you to run it from any directory.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ctf-toolkit.git
   cd ctf-toolkit
   ```
2. Install the package and dependencies:
   ```bash
   pip install -e .
   ```
   *(Note: Use `pip3` if `pip` defaults to Python 2 on your system).*

### Option B: Docker Environment
If you prefer an isolated environment pre-loaded with Kali Linux tools (nmap, ffuf, sqlmap, etc.), use Docker.

1. Navigate to the infrastructure directory:
   ```bash
   cd ctf-toolkit/infra/
   ```
2. Make the setup script executable and run it:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
   This will build the Docker image, start the container, and drop you directly into a bash shell inside the Kali environment. The `ctf-toolkit` command will be available inside the container.

---

## 3. Command Structure
The toolkit uses a nested command structure:
```bash
ctf-toolkit <module> <command> [options]
```
To see the available modules at any time, run:
```bash
ctf-toolkit -h
```

---

## 4. Module Usage & Examples

### Web Module
The web module is designed to quickly triage web parameters for common vulnerabilities like SQL Injection (SQLi) and Server-Side Template Injection (SSTI).

**Command:** `ctf-toolkit web probe`

**Options:**
- `-u, --url`: The target URL (e.g., `http://ctf.com/login`)
- `-p, --param`: The parameter to test (e.g., `username`)
- `--proxy`: (Optional) Route traffic through a proxy like Burp Suite (e.g., `http://127.0.0.1:8080`)

**Examples:**
```bash
# Quick test without proxy
ctf-toolkit web probe -u http://127.0.0.1:8080/login -p username

# Test while routing traffic through Burp Suite
ctf-toolkit web probe -u http://challenge.ctf.com/search -p query --proxy http://127.0.0.1:8080
```

### Pwn Module
The pwn module provides a boilerplate `pwntools` script. It automatically connects to a remote host and can parse a local binary to display its security protections (checksec) before sending a test payload.

**Command:** `ctf-toolkit pwn exploit`

**Options:**
- `-r, --remote`: The remote target in `host:port` format.
- `-b, --binary`: (Optional) Path to the local binary to check protections.

**Examples:**
```bash
# Connect to a remote challenge
ctf-toolkit pwn exploit -r challenge.ctf.com:1337

# Analyze a local binary and connect to remote
ctf-toolkit pwn exploit -b ./vuln_binary -r 10.10.10.5:31337
```

### Crypto Module
Quickly encode or decode strings for common CTF crypto challenges without leaving your terminal.

**Commands:** `ctf-toolkit crypto encode` or `ctf-toolkit crypto decode`

**Options:**
- `-t, --text`: The string to encode/decode.
- `-m, --mode`: The encoding type (`base64`, `hex`, `rot13`).

**Examples:**
```bash
# Decode a base64 string
ctf-toolkit crypto decode -t "ZmxhZ3t0ZXN0fQ==" -m base64

# Encode a string to hex
ctf-toolkit crypto encode -t "secret_message" -m hex

# Decode ROT13
ctf-toolkit crypto decode -t "synt{grfg}" -m rot13
```

### Reverse Engineering Module
The RE module consists of an IDAPython script rather than a CLI command. It is executed directly inside IDA Pro to save you from manually searching through thousands of strings.

**How to use:**
1. Open your target binary in IDA Pro.
2. Go to `File` -> `Script File...`.
3. Select `modules/re/ida_scripts/find_flags.py` from your project directory.
4. Check the IDA Output window. The script will print any flags found and automatically rename the function referencing the flag to `FlagChecker`.

---

## 5. Infrastructure & Docker Usage
If you used the Docker setup (`infra/setup.sh`), you have access to a fully configured Kali Linux environment.

- **Your working directory:** The `workspace/` folder inside `infra/` is mounted to `/ctf` inside the container. Download your CTF binaries and files here.
- **Catching Reverse Shells:** The Docker container uses `network_mode: "host"`. If you run a netcat listener inside the container (`nc -lvnp 4444`), it will be accessible from your host machine's IP.
- **Exiting:** Type `exit` to leave the container. The container will continue running in the background. To stop it completely, run `docker-compose down` from the `infra/` directory on your host.

---

## 6. Extending the Toolkit
The toolkit is built to be modular. To add your own custom functionality:

1. Create a new Python file in the relevant `modules/` subdirectory (e.g., `modules/web/custom_scanner.py`).
2. Write a function that accepts the `args` object from `argparse`.
3. Register the command in `core/cli.py` by adding a new subparser:
   ```python
   # Inside core/cli.py
   web_custom = web_subparsers.add_parser("custom", help="My custom web scanner")
   web_custom.add_argument("-u", "--url", required=True)
   web_custom.set_defaults(func=run_custom_scanner)
   ```

---

## 7. Troubleshooting

**Q: I get a `command not found: ctf-toolkit` error after local installation.**
A: Ensure your Python `bin` directory is in your system's PATH. Alternatively, you can run the CLI directly by executing `python3 -m core.cli` from the project root.

**Q: The web probe gives me an SSL Certificate Error when using `--proxy`.**
A: This is expected. When routing through Burp Suite, SSL verification is automatically disabled by the `proxy_handler.py` script to allow Burp to intercept HTTPS traffic seamlessly.

**Q: The `pwn exploit` command crashes when connecting to the remote server.**
A: Ensure the remote server is actually listening and you formatted the `-r` flag correctly as `host:port` (e.g., `127.0.0.1:1337`, without `http://`).
