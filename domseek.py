import sys
from colorama import init, Fore
from argparse import ArgumentParser
from utils.file_handler import load_domains
from domain_checker.checker import DomainChecker
from domain_checker.filters import apply_filters

init(autoreset=True)

def parse_arguments():
    parser = ArgumentParser(prog="domseek", description="Domain Checker")
    parser.add_argument("-l", "--list", type=str, help="path to the domain list file")
    parser.add_argument("-sc", "--status-code", type=str, help="comma-separated HTTP status code to check (e.g., 200,403)")
    parser.add_argument("-fd", "--filter-domain", type=str, help="comma-separated domain filters (e.g., com,org)")
    parser.add_argument("-ia", "--inactive", action="store_true", help="display inactive domain")
    parser.add_argument("-is", "--ignore-ssl", action="store_true", help="ignore SSL certificate errors")
    parser.add_argument("-th", "--threads", type=int, default=5, help="number of threads to use (default: %(default)s)")
    parser.add_argument("-tm", "--timeout", type=int, default=10, help="request timeout in seconds (default: %(default)s)")
    parser.add_argument("--retry", type=int, default=3, help="number of retries of each domain (default: %(default)s)")
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    valid_status_code = list(map(int, args.status_code.split(','))) if args.status_code else [200]
    
    domains = []
    if args.list:
        domains = load_domains(args.list)
        print(f"[{Fore.LIGHTBLUE_EX}!{Fore.RESET}] Checking {Fore.LIGHTGREEN_EX}{len(domains)}{Fore.RESET} domains in {args.list}")
    else:
        if sys.stdin.isatty():
            print("Error: No input provided. Use -l or pipe a list through stdin.")
            sys.exit(1)
        domains = [line.strip() for line in sys.stdin if line.strip()]
        print(f"[{Fore.LIGHTBLUE_EX}!{Fore.RESET}] Checking {Fore.LIGHTGREEN_EX}{len(domains)}{Fore.RESET} domains from STDIN")
    
    if args.filter_domain:
        filters = args.filter_domain.split(',')
        domains = apply_filters(domains, filters)
        
    checker = DomainChecker(valid_status_code, args.timeout, args.ignore_ssl, args.retry)
    results = checker.check_domains(domains, args.threads)
    inactive_domains = [domain for domain, status in results.items() if not status]
    
    for domain, status in results.items():
        if status:
            print(f"[{Fore.GREEN}{status}{Fore.RESET}] {domain}")
        else:
            print(f"[{Fore.RED}{status}{Fore.RESET}] {domain}")
        
    if args.inactive:
        for domain in inactive_domains:
            print(f"[{Fore.RED}INACTIVE{Fore.RESET}] {domain}")
    
if __name__ == "__main__":
    main()