from argparse import ArgumentParser

def parse_arguments():
    parser = ArgumentParser(prog="domseek", description="Domain Checker")
    parser.add_argument("-l", "--list", type=str, help="path to the domain list file")
    parser.add_argument("-sc", "--status-code", type=str, help="comma-separated HTTP status code to check (e.g., 200,403)")
    parser.add_argument("-fd", "--filter-domain", type=str, help="comma-separated domain filters (e.g., com,org)")
    parser.add_argument("-ia", "--inactive", action="store_true", help="display inactive domain")
    parser.add_argument("-is", "--ignore-ssl", action="store_true", help="ignore SSL certificate errors")
    parser.add_argument("-th", "--thread", type=int, default=5, help="number of threads to use (default: %(default)s)")
    parser.add_argument("-tm", "--timeout", type=int, default=10, help="request timeout in seconds (default: %(default)s)")
    parser.add_argument("--retry", type=int, default=3, help="number of retries of each domain (default: %(default)s)")
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    valid_status_code = list(map(int, args.status_code.split(','))) if args.status_code else [200]
    
if __name__ == "__main__":
    main()