class Book:
	
	def __init__(self, dictionary):
		self.dictionary = dictionary

	def add(self, name, address):
		self.dictionary[name] = address		
		return 'new entry {} : {} added'.format(name, address)

	def remove(self, name):
		address_presented = name in self.dictionary 
		if address_presented:
			del self.dictionary[name]			
			return 'entry {} deleted'.format(name)
		else:
			return 'there is no entry with key {}'.format(name)

	def find(self, name):	
		if name in self.dictionary :			
			return self.dictionary[name]
		else:
			return 'there is no entry with key {}'.format(name)
