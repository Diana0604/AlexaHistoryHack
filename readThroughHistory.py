class History :
	#Atributs: 
	#first -> indica si es el primer cop que llegeixo
	#lastCommand -> l'ultima comanda que he llegit a la crida anterior
	#page -> pagina que acabo de llegir
	#nextCommand -> comandos que vaig llegint
	#startReading -> a partir d'on pot haver-hi nous comandos
	#Debug -> per debugar
	
	
	def __init__(self):
		self.first = True
		self.lastCommand = ''
		self.startReading = 1;
		self.Debug = 1; 
		
	def historyProva(self):
		import urllib2
		user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
		headers = { 'User-Agent' : user_agent }
		req = urllib2.Request('http://alexa.amazon.co.uk/spa/index.html#settings/dialogs', None, headers)
		response = urllib2.urlopen(req)
		self.page = response.read()
		#print(self.page)
		response.close() # its always safe to close an open connection
		
		#return self.page; 
		
	def Today(self,i):
		if(self.page[i] != 's'): return False; 
		if(self.page[i+1] != 'i'): return False; 
		if(self.page[i+2] != 'm'): return False; 
		if(self.page[i+3] != 'o'): return False; 
		if(self.page[i+4] != 'n'): return False; 
		return True
			
	
	def findNextCommand(self, i):
		
		#per trobar on esta el proper Today
		while(self.Today(i) == False): 
			i = i + 1;
		
		command = []; 
		while(self.page[i] != '>'):
			command.append(self.page[i])
			i = i + 1
		
		self.startReading = i; 
		
		command = ''.join(command)
		if(self.Debug == 1): print command
		return command
		
	#def findNewCommands(self, newHistory) : #aixo sera lo bo pero per ara per fer proves faig aixi cutres
	def findNewCommands(self) :
		#looks for first new commands
		self.historyProva()
		newCommands = False; 
		while newCommands == False : 
			self.nextCommand = self.findNextCommand(self.startReading) #Todo anar fent
			
			
		
			
		
		print(self.lastCommand)
		