"""####################################################
                Imported packages
####################################################"""

import os

def wapt():
	while True:
		"""####################################################
	              Initial stage of Program
		####################################################"""
		print("-----------------------WAPT SCANNER--------------------------")
		print("""
		1.) Basic Information About Website ==> pyrecon.py  (for windows and kali)
		2.) SQL-I testing  ==>  sqli_0.py and sqli_1.py 
        	3.) Xss Testing ==> xss_0.py  
        	4.) PHP Code Execution ==> PHP_code_execution.py
        	5.) LFI ==> lfi.py 
        	6.) Open Redirection ==> Open_redirection.py
        	7.) admin finder ==> admin_finder.py
        	8.) Wordpress Testing ==> wp_scanner.py
        	0.) Want to exit?
     	""")
		a= int(input("Enter your choice: "))
		if(a == 1):
			print("----We have two type of pyrecon---")
			print("1. For Windows Operating system")
			print("2. For kali linux")
			try:	
				c = int(input("Enter your choice: "))
				if(c == 1):
					os.system("python pyrecon_window.py")
				elif(c == 2):
					os.system("python pyrecon_linux.py")
			except Exception as e:
				print("\nSomething is wrong here, please start again from begining.")
				wapt()
		elif(a == 2):
			print("Test for sqlinjection vulnerability........")
			print("1. Search in whole web link?")
			print("2. choose this if you have parametered link")
			try:	
				b = int(input("Enter your choice: "))
				if(b == 1):
					os.system("python sqli_0.py")
				elif(b == 2):
					os.system("python sqli_1.py")
			except Exception as e:
				print("\nSomething is wrong here, please start again from begining.")
				wapt()
		elif(a == 3):
			print("----XSS SCANNER is loading......")
			print("Example: http://www.microtek.com/search.php?word=")
			url = raw_input("Enter url: ")
			try:
				os.system("python xss_0.py "+"-u "+url)
			except Exception as e:
				print("\nSomething is wrong here, please start again from begining.")
				wapt()			
		elif(a == 4):
			print("Example: http://www.microtek.com/search.php?word=")
			try:
				os.system("python PHP_code_execution.py")
			except Exception as e:
				print("\nSomething is wrong here, please start again from begining.")
				wapt()
		elif(a == 5):
			print("Example: http://www.microtek.com/")
			try:
				os.system("python lfi.py")
			except Exception as e:
				print("\nSomething is wrong here, please start again from begining.")
				wapt()
		elif(a == 6):
			print("""----Open Redirection Testing......
				Payloads example
				payload = //www.google.com/%2F..
				payload2 = //www.yahoo.com//
				payload3 = //www.yahoo.com//%2F%2E%2E
				""")
			try:
				url = raw_input("Enter Website url(http://www.xyz.com)  Or Enter .list file(websites.list): ")
				payload= raw_input("Enter payload : ")
				os.system("python Open_redirection.py "+url+" "+payload)
			except Exception as e:
				print("\nSomething is wrong here, please start again from begining.")
				wapt()
		elif(a == 7):
			print("Example: http://www.microtek.com")
			try:
				os.system("python admin_finder.py")
			except Exception as e:
				print("\nSomething is wrong here, please start again from begining.")
				wapt()			
		elif(a == 8):
			try:
				os.system("python wp_scanner.py")
			except Exception as e:
				print("\nSomething is wrong here, please start again from begining.")
				wapt()
		elif(a == 0):
			False
			exit()
try:
	wapt()
except Exception as e:
	print("\nSomething is wrong here, please start again from begining.")
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"