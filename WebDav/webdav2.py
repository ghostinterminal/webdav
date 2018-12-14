import requests
from bs4 import BeautifulSoup
import sys,time

			# The webdav2.py file is used to check the availability of check all the requests founded in a seed url as well as seed url.




URL_LIST = []


url = str(sys.argv[1])
br = requests.get(url, headers={'User-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'})
data = br.text
soup = BeautifulSoup(data, 'lxml')
links = soup.find_all('a')
for link in links:
    try:
    	l = str(link['href'])
    	if l.startswith('#'):
        	pass
    	else:
        	URL_LIST.append(l)
    except:
	  pass


print "Total Links: ",len(URL_LIST)
print '------------------------------------------------------'*2
print 'Started at {0}'.format(time.ctime())

def checkMethods(url):
	if url == "/":
		pass
	methods = ['Put', 'Get', "Post", 'Search', 'Connect', 'Propfind', 'Copy', 'Options', 'Trace', 'Delete', 'Move', 'Mkcol', 'Head', 'Proppatch', 'Lock', 'Unlock', 'Search',]
	try:
		print '------------------------------------------------------'*2
		print '|Method|			|Code|				|Url|'
		print '------------------------------------------------------'*2
		try:
			for method in methods:
				req = requests.request(str(method), url)
				print '{0}				 {1}				 {2}'.format(method, req.status_code, url)
		except:
			pass
		print '------------------------------------------------------'*2
		print ''*2
	except:
		pass

for url in URL_LIST:
	try:
		checkMethods(url)
	except:
		sys.exit()
