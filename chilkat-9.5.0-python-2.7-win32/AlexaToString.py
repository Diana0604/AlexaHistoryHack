

def readAlexa():
	Debug = 1; 
	import chilkat
	htmlToText = chilkat.CkHtmlToText()
	# filename is a string
	# srcCharset is a string
	# outStr is a CkString (output)
	filename = 'Alexa2.htm'
	srcCharset = 'utf-8'
	outStr = chilkat.CkString()
	status = htmlToText.ReadFileToString(filename, srcCharset, outStr);
	retStr = htmlToText.readFileToString(filename, srcCharset);
	print(retStr)
	if status == True:
		
		retStr = htmlToText.readFileToString(filename, srcCharset);
		print(retStr)
		if(Debug == 1): print('in the variable retStr there is the html text')
	if status == False:
		if(Debug == 1): print('Something went wrong')

#def searchForSimon():
	
		
#if __name__ == "__main__":
#    import sys
#    fib(int(sys.argv[1]))