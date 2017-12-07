import os

try:
	print("------WpScanner - scanning in wordpress website-------")
	a = raw_input("Enter your website (Example: www.xyz.com): ")
	os.system("wpscan "+"--url "+a)
except Exception as e:
	print("\nSomething is wrong here, please start again from begining.")
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"