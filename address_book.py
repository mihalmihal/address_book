import sys
from book import Book
from storage import Storage


command = sys.argv[1]
args_len = len(sys.argv);

storage = Storage().getDictionary()
book = Book(storage)
result = ''
if command == 'add':	

	if args_len < 4: 
		result = 'to few arguments passed'
	else:
		result = book.add(sys.argv[2], sys.argv[3])
		Storage().storeDictionary(book.dictionary)
elif command == 'remove':

	if args_len < 3: 
		result = 'to few arguments passed'
	else:
		result = book.remove(sys.argv[2])
		Storage().storeDictionary(book.dictionary)
elif command == 'find':

	if args_len < 3: 
		result = 'to few arguments passed'
	else:
		result = book.find(sys.argv[2])

else: 

	result = 'command {} not found'.format(sys.argv[1])

print(result)