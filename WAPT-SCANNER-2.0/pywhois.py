import whois
domain = whois.query("google.com")

print(domain.__dict__)