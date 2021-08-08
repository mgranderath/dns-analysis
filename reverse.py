import dns.reversename
import dns.resolver

def convertToLookup(ip):
    try:
        answer = dns.resolver.resolve_address(ip)
        return { "ip": ip, "domain": str(answer[0]) }
    except:
        return None