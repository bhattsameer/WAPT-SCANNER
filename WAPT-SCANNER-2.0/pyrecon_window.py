import requests
from tld import get_tld
import os
import urllib
import io,sys

url = sys.argv[1]


def http_header():
    r = requests.head(url)
    print('Status code: ' + str(r.status_code) + '\n')
    print('Server Header: \n')
    f = open('pyrecon_header.txt', 'w')
    for x in r.headers:
        f.write('Status code: ' + str(r.status_code) + '\n'+'\t'+ '%s : %s' % (x, r.headers[x]))
        
try:
    http_header()

except Exception as e:
    print("\nSomething is wrong here, please start again from begining.")
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"