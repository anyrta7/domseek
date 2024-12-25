def apply_filters(domains, filters):
    filtered_domains = []
    for domain in domains:
        if any(f in domain for f in filters):
            filtered_domains.append(domain)
    return filtered_domains