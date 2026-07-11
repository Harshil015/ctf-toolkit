# IDAPython Script: Run this inside IDA Pro (File -> Script File)
# This script scans all strings in the binary for common CTF flag formats
# and renames functions that reference those strings.

import idautils
import idc
import re

# Define common CTF flag regex patterns
FLAG_PATTERNS = [
    r"flag\{.*?\}",
    r"ctf\{.*?\}",
    r"picoCTF\{.*?\}",
    r"HTB\{.*?\}",
    r"FLAG\{.*?\}"
]

def find_flag_strings():
    print("[*] Scanning for flag strings in IDA Pro...")
    found = False
    for s in idautils.Strings():
        for pattern in FLAG_PATTERNS:
            if re.match(pattern, str(s)):
                print(f"[+] FOUND FLAG: {s} at address {hex(s.ea)}")
                found = True
                
                # Find cross-references to this string and rename the parent function
                for xref in idautils.XrefsTo(s.ea):
                    func_addr = idc.get_func_attr(xref.frm, idc.FUNCATTR_START)
                    if func_addr != idc.BADADDR:
                        old_name = idc.get_func_name(func_addr)
                        idc.set_name(func_addr, "FlagChecker", idc.SN_NOWARN)
                        print(f"    [+] Renamed function at {hex(func_addr)} (was {old_name}) to FlagChecker")
    if not found:
        print("[-] No flags found in strings.")

if __name__ == "__main__":
    find_flag_strings()
