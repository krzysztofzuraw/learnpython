from bs4 import BeautifulSoup
import urllib.request
import re
import ipaddress

def ip_lookup(addr):
    """
    Simple ip information from whois'
    :param addr: ip address
    :return: dictionary of {ip, host name, country}
    :rtype: dictionary
    """
    try:
        ipaddress.ip_address(addr)
    except ValueError:
        return ("Something is wrong with ip address, try one more time")

    page = urllib.request.urlopen("https://who.is/whois-ip/ip-address/" + addr )

    soup = BeautifulSoup(page)

    full_doc = soup.find_all('pre')


    regex = re.compile("netname:[\s]+([\w-]+).+country:[\s]+([\w]+)", re.DOTALL)
    extract = regex.search(str(full_doc))

    result = {'ip': addr, 'host name': extract.group(1), 'country' : extract.group(2) }
    
    return result


def www_lookup(website):
    """
    Get website ip from whois
    """
    page = urllib.request.urlopen("https://who.is/whois/" + website)
    soup = BeautifulSoup(page)
    for node in soup.find_all(attrs={"data-bind-domain":"ip_address"}):
        addr = ''.join(node.find_all(text=True)).strip()
    return ip_lookup(addr)

    

