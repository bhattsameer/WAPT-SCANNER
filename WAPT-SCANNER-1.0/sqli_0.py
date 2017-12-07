from bs4 import BeautifulSoup
import urllib
import mechanize

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
try:
  url = raw_input("Enter website url: ")

  html = urllib.urlopen(url)
  bt = BeautifulSoup(html.read(),"lxml")
  allLinks = bt.find_all('a')
  a = []

  for links in allLinks:
      if "=" in links['href']:
          url2=url+links['href']+"'"
          a.append(url2)
  i=0
  for i in range(0,len(a)):
      url3=str(a[i])
      print(url3)
      html2 = urllib.urlopen(url3)
      bt2 = BeautifulSoup(html2.read(),"lxml")
      if "You have an error in your SQL syntax" in bt2.get_text():
          print("-->>> ABOVE URL IS VULNERABLE WITH SQL INJECTION")
          print('\n')
      else:
          print("-->>> ABOVE URL IS NOT-VULNERABLE WITH SQL INJECTION")
          print('\n')
except Exception as e:
  print("\nSomething is wrong here, please start again from begining.")
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"