import requests
import sys,time

print '''\n
				
							|HELP MENU|

		The webdav3.py file is used to retrieve headers and length of data from websites using different requests.

		\n
'''





if len(sys.argv) != 2:
	print "HELP: python webdav3.py <url>"

url = sys.argv[1]

print time.ctime()
print ''

methods = ['Put', 'Get', "Post", 'Search', 'Connect', 'Propfind', 'Copy', 'Options', 'Trace', 'Delete', 'Move', 'Mkcol', 'Head', 'Proppatch', 'Lock', 'Unlock', 'Search',]



def checkMethods(method,url):
	req = requests.request(str(method), str(url))

	print '---------------------------------------------'*2
	print '|Showing Headers by having {0} method.'.format(method)
	print '---------------------------------------------'*2
	print req.headers
	print ''
	print "Length of data founded, ",len(req.text)
	print ''


for method in methods:
	checkMethods(method, url)


