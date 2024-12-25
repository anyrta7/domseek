import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

class DomainChecker:
    def __init__(self, status_code, timeout, ignore_ssl, retry):
        self.status_code = status_code
        self.timeout = timeout
        self.ignore_ssl = ignore_ssl
        self.retry = retry
    
    def _ensure_scheme(self, domain):
        parsed = urlparse(domain)
        if not parsed.scheme:
            return f"http://{domain}"
        return domain
    
    def _check_domain(self, domain):
        domain = self._ensure_scheme(domain)
        for _ in range(self.retry):
            try:
                response = requests.get(domain, timeout=self.timeout, verify=not self.ignore_ssl)
                if response.status_code in self.status_code:
                    return response.status_code
            except requests.RequestException:
                continue
        return None
    
    def check_domains(self, domains, threads):
        results = {}
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = {executor.submit(self._check_domain, domain): domain for domain in domains}
            for future in futures:
                domain = futures[future]
                results[domain] = future.result()
            return results