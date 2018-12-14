import requests
import sys, time,os


cmd_help = '''\n
		--------------------------------------------------------------	
		|Command| 			|What it do|					
		--------------------------------------------------------------
		|content			Show content founded in page.	
		|headers 			Show headers.					
		|text 				Show text.						
		|status				Show status_code
		|nm 				Start Using new method
		|new 				Start New Session
		|clear 				Clear the Terminal  				
		-------------------------------------------------------------
'''

def he_lp():
	print cmd_help
	print ""
	print 'Rerun the script.....'
	print 'Learn all the commands before starting...'
	print 'Otherwise you will do the same thing again....'
	print 'Thanks'
	print '...................'
	print 'from ghostinterminal.'


def simulate(method, url):
	req = requests.request(str(method), url)
	url = url
	print ''
	while True:
		cmd = raw_input("<#SiMuLaTiNgShElL#> ")
		# If nesting...
		if cmd.lower() == "help":
			he_lp()

		if cmd.lower() == "content":
			print req.content

		if cmd.lower() == "text":
			print req.text


		if cmd.lower() == "status":
			print req.status_code


		if cmd.lower() == "headers":
			print req.headers

		if cmd.lower() == "new":
			print '\nGoing to main\n'
			os.system('clear')
			return main()
		if cmd.lower() == "clear":
			os.system('clear')

		if cmd.lower() == "nm":
			os.system('clear')
			m = raw_input("Enter New Method: ")
			simulate(m, url)







def main():
	url = raw_input("Enter url: ")
	method = raw_input("Enter method to Simulate: ")
	try:
		simulate(method, url)
	except Exception as e:
		return e

main()