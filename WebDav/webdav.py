import socket
import requests
import argparse


arguments = argparse.ArgumentParser()
arguments.add_argument("-u","--url",type=str, help="ENTER THE URL")

arg = arguments.parse_args() #Arguments are parsed here.


def checkMethods():
	methods = ['Put', 'Get', "Post", 'Search', 'Connect', 'Propfind', 'Copy', 'Options', 'Trace', 'Delete', 'Move', 'Mkcol', 'Head', 'Proppatch', 'Lock', 'Unlock', 'Search',]
	print '------------------------------------------------------'
	print '|Method|		|Code|'
	print '------------------------------------------------------'
	for method in methods:
		req = requests.request(str(method), arg.url)
		print '{0}		 	 {1}'.format(method, req.status_code)
	print '------------------------------------------------------'

checkMethods()


