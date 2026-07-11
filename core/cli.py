#!/usr/bin/env python3
import argparse
import sys
from core.utils import print_banner
from modules.web.scanner import run_web_probe
from modules.pwn.exploit_template import run_pwn_exploit
from modules.crypto.encoding_tools import run_crypto_tool

def main():
    print_banner()
    parser = argparse.ArgumentParser(
        description="CTF Automation Toolkit",
        usage="ctf-toolkit <module> <command> [options]"
    )
    
    subparsers = parser.add_subparsers(dest="module", help="Available modules")

    # Web Module Parser
    web_parser = subparsers.add_parser("web", help="Web exploitation tools")
    web_subparsers = web_parser.add_subparsers(dest="command", required=True)
    
    web_probe = web_subparsers.add_parser("probe", help="Quick test parameters for SQLi/SSTI")
    web_probe.add_argument("-u", "--url", required=True, help="Target URL (e.g., http://localhost/login)")
    web_probe.add_argument("-p", "--param", required=True, help="Parameter to test (e.g., username)")
    web_probe.add_argument("--proxy", default=None, help="Proxy URL (e.g., http://127.0.0.1:8080)")
    web_probe.set_defaults(func=run_web_probe)

    # Pwn Module Parser
    pwn_parser = subparsers.add_parser("pwn", help="Binary exploitation tools")
    pwn_subparsers = pwn_parser.add_subparsers(dest="command", required=True)

    pwn_exploit = pwn_subparsers.add_parser("exploit", help="Run pwntools template")
    pwn_exploit.add_argument("-r", "--remote", required=True, help="Remote host:port (e.g., 127.0.0.1:1337)")
    pwn_exploit.add_argument("-b", "--binary", default=None, help="Local binary path for checksec (optional)")
    pwn_exploit.set_defaults(func=run_pwn_exploit)

    # Crypto Module Parser
    crypto_parser = subparsers.add_parser("crypto", help="Quick crypto encoding/decoding tools")
    crypto_subparsers = crypto_parser.add_subparsers(dest="command", required=True)

    crypto_encode = crypto_subparsers.add_parser("encode", help="Encode a string")
    crypto_encode.add_argument("-t", "--text", required=True, help="Text to encode")
    crypto_encode.add_argument("-m", "--mode", required=True, choices=["base64", "hex", "rot13"], help="Encoding mode")
    crypto_encode.set_defaults(func=run_crypto_tool, action="encode")

    crypto_decode = crypto_subparsers.add_parser("decode", help="Decode a string")
    crypto_decode.add_argument("-t", "--text", required=True, help="Text to decode")
    crypto_decode.add_argument("-m", "--mode", required=True, choices=["base64", "hex", "rot13"], help="Decoding mode")
    crypto_decode.set_defaults(func=run_crypto_tool, action="decode")

    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
