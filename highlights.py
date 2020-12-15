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
	split1 = info.split(' ')
	split2= split1[5].split('-')
	location = int(split2[0] + split2[1])
	return location

def read_clippings():
	count = 0
	raw_highlight_info = []
	highlight_num = 0
	all_highlights = []

	with open('clippings', 'rt') as myfile:
		for line in myfile:
			if line[0] == '\n' or line[0] == '=':
				continue
			else:
				if count < 3:
					raw_highlight_info.append(line.rstrip('\n'))
					count += 1
					if count == 3:
						highlight_num += 1
						all_highlights.append(raw_highlight_info)
						count = 0
						raw_highlight_info = []
		return highlight_num, all_highlights

def remove_dups(highlight_num, all_highlights):
	i = 0
	while i < highlight_num - 1:
		if abs(find_location(all_highlights[i][1]) - find_location(all_highlights[i + 1][1])) < 10:
			all_highlights.pop(i)
			highlight_num -= 1
		else:
			i += 1
	return highlight_num

def create_library(highlight_num, all_highlights):
	library = []
	i = 0
	found = 0
	while i < highlight_num:
		for j in library:
			if all_highlights[i][0] == j.get_title_auth():
				j.add_highlight(all_highlights[i][2])
				found = 1
		if found == 0:
			library.append(Book(all_highlights[i][0], []))
			library[len(library) - 1].add_highlight(all_highlights[i][2])

		found = 0
		i += 1

	return library

def main():
	highlight_num, all_highlights = read_clippings()
	new_highlight_num = remove_dups(highlight_num, all_highlights)
	library = create_library(new_highlight_num, all_highlights)

	print("Welcome To Your Highlight Library!")

	for book in library:
		print('[' + str(library.index(book) + 1) + '] ' + book.get_title_auth()) 

	book_index = int(input("What Book Would You Like To View? "))
	print("")

	print(library[book_index - 1].get_title_auth())
	print("----------\n")
	for highlight in library[book_index - 1].get_highlights():
		print(highlight, '\n')

	menu = input("Would You Like To Return To Main Menu? (Y/N) ")
	print()
	if menu == 'Y':
		main()
	
main()
