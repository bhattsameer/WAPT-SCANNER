#!/usr/bin/env python
import requests,sys,time,os
top = """
 #################################################
 # Open redirect Scanner for dummies like me :)  #
 #################################################
    """

def main():
    os.system('cls')

    print(top)

    # Payloads example
    # This is replaced with a payloads.list (a lot of amazing redirect payloads)
    #payload = '//www.google.com/%2F..'
    #payload2 = '//www.yahoo.com//'
    #payload3 = '//www.yahoo.com//%2F%2E%2E'

    # first argument - file with subdomains

    file = sys.argv[1]

    # second argument - payload string

    payload = sys.argv[2]



    #open file with subdomains and iterates
 
    with open(file) as f:

		print ""
		print "Searching...."
		print ""
		time.sleep(4)


		# loop for find the trace of all requests (303 is an open redirect) see the final destination

                for line in f:
		    

                    try:

                        if 'http://' or 'https://' in line:
                            line2 = line.strip()
                            line3 = line2 + payload
                            print line3

                        response = requests.get(line3, verify=True)    

                        print response

                        try:

                            if response.history:
                             
                                print "Request was redirected"
                             
                                for resp in response.history:

                                    print "|"
                                    print resp.status_code, resp.url
                                    

                                print "Final destination:"

                                print "+"
                                print response.status_code, response.url

                                
                            else:

                                print "Request was not redirected"

                            
                        except:
                            print "connection error :("

                    except:

                        print "quitting.."
                        print(" Url must be in format of http://www.xyz.com")
                        

try:
	main()
except IndexError:
	print(" Usage: python "+sys.argv[0]+" [subdomains.file] [redirect.payload]\n")
        print(" Example python "+sys.argv[0]+" uber.list '//yahoo.com/%2F..'\n")
except Exception as e:
    print("\nSomething is wrong here, please start again from begining.")
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"