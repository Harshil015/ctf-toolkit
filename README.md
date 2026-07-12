# CTF Automation Toolkit

A modular CLI tool that unifies web, pwn, crypto, and reverse-engineering workflows under a single command — built to eliminate the repetitive setup that eats into actual CTF solving time.

---

## Why I built this

Every CTF resets the same repetitive setup: a one-off script to test SQLi on a login form, a fresh pwntools boilerplate for every new binary, base64 decoded by hand for the tenth time that week. I built this toolkit to collapse that setup into one consistent command, so more time goes into solving the challenge and less into re-writing the same scaffolding.

---

## What it does

| Module | Purpose |
|---|---|
| **Web** | Probes parameters for SQL injection and SSTI, with optional Burp Suite proxy routing |
| **Pwn** | Pwntools boilerplate that runs checksec against a local binary before connecting to the remote target |
| **Crypto** | Encodes/decodes base64, hex, and ROT13 without leaving the terminal |
| **Reverse Engineering** | An IDAPython script that scans a binary's strings inside IDA Pro and auto-renames the function referencing a found flag |

All four run through one entry point:

```
ctf-toolkit <module> <command> [options]
```

---

## Architecture

```
core/       — CLI entry point and argument parsing (argparse, extensible subparsers)
infra/      — Docker environment definition, preloaded with Kali Linux tools (nmap, ffuf, sqlmap)
modules/    — one subdirectory per capability: web, pwn, crypto, re
wordlists/  — fuzzing resources used by the web module
setup.py    — packages the tool as a pip-installable CLI
```

---

## Tech stack

| Component | Tool |
|---|---|
| Language | Python |
| Exploitation | pwntools |
| Reverse engineering | IDAPython (IDA Pro) |
| Containerization | Docker, Docker Compose |
| Base image | Kali Linux (nmap, ffuf, sqlmap) |
| Interception | Burp Suite-compatible proxy routing |
| CI/CD | GitHub Actions |

---

## Setup

**Option A — Local installation**

```bash
git clone https://github.com/Harshil015/ctf-toolkit.git
cd ctf-toolkit
pip install -e .
```

**Option B — Docker (Kali Linux preloaded)**

```bash
cd ctf-toolkit/infra/
chmod +x setup.sh
./setup.sh
```

Drops you into a bash shell inside a ready-to-go Kali container with `ctf-toolkit` already on the PATH.

---

## Quick example

```bash
# Probe a login parameter for SQLi, routed through Burp Suite
ctf-toolkit web probe -u http://challenge.ctf.com/login -p username --proxy http://127.0.0.1:8080
```

Full command reference for all four modules, Docker networking details, and troubleshooting: see [`User_Manual.md`](User_Manual.md).

---

## Extending the toolkit

Built to be modular — new capability drops into `modules/`, then registers as an argparse subcommand in `core/cli.py`. Full walkthrough in the User Manual.

---

## Limitations

- Reverse engineering module requires IDA Pro specifically — no free-alternative (Ghidra) support yet
- Crypto module currently covers base64, hex, and ROT13 only
- Docker setup uses host networking for reverse-shell catching, which trades some container isolation for convenience — not intended for untrusted binaries without additional sandboxing

---

## Roadmap

- [ ] Ghidra support for the reverse engineering module
- [ ] Additional crypto encodings (XOR, Caesar brute-force, RSA helpers)
- [ ] Automated per-run report generation summarizing findings across modules
- [ ] Custom wordlist injection per target for the web module

---

## Legal disclaimer

Built for authorized CTF competitions, bug bounty programs operating within defined scope, and personal lab environments. Do not use against any system or target without explicit authorization.

---

## Author

**Harshil Makwana** — ECE graduate from SVNIT Surat, building security tools and looking for a first role in penetration testing, VAPT, or SOC.

[linkedin.com/in/harshilmakwana](https://linkedin.com/in/harshilmakwana) · [github.com/Harshil015](https://github.com/Harshil015)
