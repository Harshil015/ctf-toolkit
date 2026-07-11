from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = r"""
     ____ _____ ____   ____ _   _ ___ _   _ _____ ____
    / ___|_   _|  _ \ / ___| | | |_ _| \ | | ____/ ___|
    \___ \ | | | |_) | |   | |_| || ||  \| |  _| \___ \
     ___) || | |  _ <| |___|  _  || || |\  | |___ ___) |
    |____/ |_| |_| \_\\____|_| |_|___|_| \_|_____|____/
    """
    print(f"{Fore.BLUE}{banner}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[+] CTF Automation Toolkit{Style.RESET_ALL}\n")
