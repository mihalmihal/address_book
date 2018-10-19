import pickle
import os

class Storage:

	filename = 'address_book'

	@classmethod
	def getDictionary(cls):
		dictionary_size = os.stat(cls.filename).st_size		

		if dictionary_size == 0:
			return {}

		file = open(cls.filename, 'rb')	
		dictionary = pickle.load(file)
		file.close()
		return dictionary

	@classmethod
	def storeDictionary(cls, dictionary):		
		file = open(cls.filename, 'w+b')		
		pickle.dump(dictionary, file)
		file.close()