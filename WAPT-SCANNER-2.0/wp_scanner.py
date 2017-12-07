import os,sys

def create_report(data):
    Write_file('wpscanner_output.txt', data)

def Write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

url = sys.argv[1]

def wpscanner():	
	print("------WpScanner - scanning in wordpress website-------")
	process = os.popen("python wpscan/main.py "+"-u "+url)
	result = str(process.read())
	create_report(result)

wpscanner()
#except Exception as e:
#	print("\nSomething is wrong here, please start again from begining.")
#except (KeyboardInterrupt, SystemExit):
 #   print "\nScan Aborted By User"