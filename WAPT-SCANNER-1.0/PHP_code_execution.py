from bs4 import BeautifulSoup
import urllib
import mechanize

print("""
    ###############################################################
                        PHP Code Execution SCANNER              
    ###############################################################
     """)

def PHP_Code_Execution_scanner(url):
    #Verify if site is vulnerable or not?
    html = urllib.urlopen(url+"<form><h1><button>PHP Code</button></h1></form>")
    bt = BeautifulSoup(html.read(),"lxml")
    if bt.find("form"):
        if bt.find("h1"):
            if bt.find("button"):
                print("-->>> ABOVE URL IS FOUND VULNERABLE WITH PHP Code Execution")
                print('  Follow Below URL')
                print("  "+url+"<form><h1><button>PHP Code</button></h1></form>\n")
    else:
        print("-->>> ABOVE URL IS NOT-VULNERABLE WITH PHP Code Execution")
        print('\n')

try:                
    web_url = raw_input("Enter test url: ")
    PHP_Code_Execution_scanner(web_url)
except Exception as e:
    print("\nSomething is wrong here, please start again from begining.")
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"																										