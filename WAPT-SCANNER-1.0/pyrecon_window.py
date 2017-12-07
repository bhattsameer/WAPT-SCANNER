import requests
from tld import get_tld
import os
import urllib
import io

def http_header(url):
	r = requests.head(url)
	print r.url
	print 'Status code: ' + str(r.status_code) + '\n'

	print 'Server Header: \n'
	for x in r.headers:
	    print '\t'+ x + ':' + r.headers[x]

def get_ip_address(url):
    command = "host" + url
    process = os.popen(command)
    resutls = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]

def get_nmap(options, ip):
    command = "nmap" + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results

try:
    url= raw_input('Enter url (Exmple: http://www.microtek.com): ')
    http_header(url)
    ip_address = get_ip_address(url)
    nmap = get_nmap('-F', ip_address)

except Exception as e:
    print("\nSomething is wrong here, please start again from begining.")
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"