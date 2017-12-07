from bs4 import BeautifulSoup
import urllib
import mechanize,sys

url = sys.argv[1]

def create_report(data):
    Write_file('lfi.txt', data)

def Write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


print("""
    ###############################################################
                        LFI VULNERABILITY SCANNER              
    ###############################################################
     """)

def lfi_scanner():
    #Verify if site is vulnerable or not?
    html = urllib.urlopen(url+"../")
    bt = BeautifulSoup(html.read(),"lxml")
    if "include(): Failed opening" in bt.get_text():
        create_report("ABOVE URL IS FOUND VULNERABLE WITH Local File inclusion")
        print('\n')
    else:
        create_report("ABOVE URL IS NOT-VULNERABLE WITH LFI")
        print('\n')
try:                
    lfi_scanner()
except Exception as e:
    print("\nSomething is wrong here, please start again from begining.")
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"
