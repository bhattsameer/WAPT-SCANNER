from tld import get_tld
import os
import urllib
import io

print ("------------PYTHON RECON---------------")

ROOT_DIR = 'compines'
create_dir(ROOT_DIR)

def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(url)
    nmap = get_nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots_txt, whois)

def create_report(name, url, domain_name, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    Write_file(project_dir + '/full_url.txt', full_url)
    Write_file(project_dir + '/domain_name.txt', domain_name)
    Write_file(project_dir + '/nmap.txt', nmap)
    Write_file(project_dir + '/robots_txt.txt', robots_txt)
    Write_file(project_dir + '/whois.txt', whois)

#1.) domain name ....

def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name

#2.) general create files

def Create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def Write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#3.) get_ip_address

def get_ip_address(url):
    command = "host" + url
    process = os.popen(command)
    resutls = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]

#4.) nmap tool

def get_nmap(options, ip):
    command = "nmap" + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results

#5.) get_robort.txt

def get_robots_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = urllib.request(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()

#6.) Whois info

def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    return results

url = input("Enter url: ")
name = input("Enter project name: ")
gather_info(name, url)