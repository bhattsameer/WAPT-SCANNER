from bs4 import BeautifulSoup
import urllib
import mechanize

print("""
    ###############################################################
                        LFI VULNERABILITY SCANNER              
    ###############################################################
     """)

def lfi_scanner(url):
    #Verify if site is vulnerable or not?
    html = urllib.urlopen(url+"../")
    bt = BeautifulSoup(html.read(),"lxml")
    
    if "include(): Failed opening" in bt.get_text():
        print("-->>> ABOVE URL IS FOUND VULNERABLE WITH Local File inclusion")
        print('\n')
    else:
        print("-->>> ABOVE URL IS NOT-VULNERABLE WITH LFI")
        print('\n')
try:                
    web_url = raw_input("Enter test url: ")
    lfi_scanner(web_url)
except Exception as e:
    print("\nSomething is wrong here, please start again from begining.")
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"
