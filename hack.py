import urllib2
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request('file:///Users/camibrumar/Desktop/Amazon%20Alexa.htm', None, headers)
response = urllib2.urlopen(req)
page = response.read()
response.close() # its always safe to close an open connection

print page
# while loop to refresh the html

import time 
while True:
	response = urllib2.urlopen(req)
	page1 = response.read()
	response.close()
	if page == page1:
		print "equal"
	else:
		print "not equal"
	page = page1
	time.sleep(5)
