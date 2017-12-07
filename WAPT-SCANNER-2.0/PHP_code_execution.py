from bs4 import BeautifulSoup
import urllib
import mechanize,sys

print("""
    ###############################################################
                                  HTML-I              
    ###############################################################
     """)

url = sys.argv[1]

def create_report(data):
    Write_file('PHP_code_execution.txt', data)

def Write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def PHP_Code_Execution_scanner():
    #Verify if site is vulnerable or not?
    html = urllib.urlopen(url+"<form><h1><button>PHP Code</button></h1></form>")
    bt = BeautifulSoup(html.read(),"lxml")
    if bt.find("form"):
        if bt.find("h1"):
            if bt.find("button"):
                print('  Follow Below URL')
                create_report(" -->>>URL IS FOUND VULNERABLE WITH PHP Code Execution "+url+"<form><h1><button>PHP Code</button></h1></form>\n")
    else:
        create_report("-->>> URL IS NOT-VULNERABLE WITH PHP Code Execution")
        print('\n')

try:                
    PHP_Code_Execution_scanner()
except Exception as e:
    print("\nSomething is wrong here, please start again from begining.")
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"																										