
import httplib
import socket
import sys

try:
	print "-----------ADMIN PANNEL FINDER-----------"
	
	var1=0
	var2=0

	regular = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','_admin/','usuarios/',
'usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html', 'adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']  

	try:
		site = raw_input("Enter the target website: ")
		site = site.replace("http://","")
		print ("Checking if website is online " + site )
		conn = httplib.HTTPConnection(site)
		conn.connect()
		print "Website is online."
	except (httplib.HTTPResponse, socket.error) as Exit:
		print("Error occured, Website offline or invalid URL")
	   	exit()
	print("Scanning " + site + "...\n")
	for admin in regular:
		admin = admin.replace("\n","")
		admin = "/" + admin
		host = site + admin
		print (" Checking " + host )
		connection = httplib.HTTPConnection(site)
		connection.request("GET",admin)
		response = connection.getresponse()
		var2 = var2 + 1

		if response.status == 200:
			var1 = var1 + 1
			print "%s %s" % ( "\n" + host, "Admin page found!")
			raw_input("Press enter to continue scanning.\n")
		elif response.status == 404:
			var2 = var2
		elif response.status == 302:
			print "%s %s" % (" " + host, "Possible admin page (302 - Redirect)")
		else:
			print "%s %s %s" % (" " + host, " Interesting response:", response.status)
		connection.close()
   	print("\nScan Completed \n")
   	print var1, " Admin pages found"
   	print var2, " Total pages checked"
except (httplib.HTTPResponse, socket.error):
	print "\nNetwork error occured! Check internet settings"
except (KeyboardInterrupt, SystemExit):
    print "\nScan Aborted By User"
