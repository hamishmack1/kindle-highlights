class Book:
	def __init__(self, title_auth, highlights):
		self.title_auth = title_auth
		self.highlights = highlights
	
	def get_title_auth(self):
		return self.title_auth
	
	def get_highlights(self):
		return self.highlights

	def add_highlight(self, highlight):
		self.highlights.append(highlight)

def find_location(info):
	split = (info.split(' '))[5].split('-')
	location = int(split[0] + split[1])
	return location

def read_clippings():
	data = open('clippings').read().strip().split('\n')
	data = [y for y in [x for x in data if x != ''] if y[0] != '=']
	data = [data[n:n+3] for n in range(0, len(data), 3)]
	return data

def create_library(all_highlights):
	i = 0
	library = []
	books = []
	while i < len(all_highlights):
		if i < len(all_highlights) - 1:
			if abs(find_location(all_highlights[i][1]) - find_location(all_highlights[i + 1][1])) < 10:
				all_highlights.pop(i)
				continue;
		if all_highlights[i][0] in books:
			library[books.index(all_highlights[i][0])].add_highlight(all_highlights[i][2])
		else:
			books.append(all_highlights[i][0])
			library.append(Book(all_highlights[i][0], []))
			library[len(library) - 1].add_highlight(all_highlights[i][2])
		i += 1
	return library

def main():
	library = create_library(read_clippings())

	print("Welcome To Your Highlight Library!")

	for book in library:
		print('[' + str(library.index(book) + 1) + '] ' + book.get_title_auth()) 

	book_index = int(input("What Book Would You Like To View? ")) - 1
	print("")

	print(library[book_index].get_title_auth() + '\n' +  "----------\n")
	for highlight in library[book_index].get_highlights():
		print(highlight, '\n')

	menu = input("Would You Like To Return To Main Menu? (Y/N) ")
	print()
	if menu == 'Y':
		main()
	
main()
