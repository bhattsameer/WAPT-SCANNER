from bs4 import BeautifulSoup
import urllib
import mechanize
import sys,os

url = sys.argv[1]

def sqli_0():
  try:

    html = urllib.urlopen(url)
    bt = BeautifulSoup(html.read(),"lxml")
    allLinks = bt.find_all('a')
    a = []

    for links in allLinks:
        if "=" in links['href']:
            url2=url+links['href']+"'"
            a.append(url2)
    i=0
    url4 = []
    f = open('sqli_0.txt','w')
    print("\nLoading...!")
    for i in range(0,len(a)):
        url3=str(a[i])
        html2 = urllib.urlopen(url3)
        bt2 = BeautifulSoup(html2.read(),"lxml")
        if "You have an error in your SQL syntax" in bt2.get_text():
            print("Found a SQL-I vulnerable link")
            f.write("URL IS VULNERABLE WITH SQL INJECTION "+url3+"\n")

  except Exception as e:
    print("\nSomething is wrong here, please start again from begining.")
  except (KeyboardInterrupt, SystemExit):
      print "\nScan Aborted By User"

print("""
          #######     #########       ##               ###########
          ##   ##     ##     ##       ##                   ##
          ##          ##     ##       ##                   ##
          #######     ##     ##       ##        ###        ##
               ##     ##  #  ##       ##                   ##
          ##   ##     ##   ####       ##                   ##
          #######     #######  ##     ##########       ###########
     """)
print("example: http://www.microtek.com/")

sqli_0()
