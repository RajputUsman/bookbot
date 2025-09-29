from stats import words_in_book, sortChars

import sys

def get_book_text(filepath):

	details = ""
	with open(filepath) as f:
		details = f.read()
		# print(details)
		words, chars = words_in_book(details)
		return details, words, chars

def main():

	if len(sys.argv) <= 1:
		print("Usage: python3 main.py <path_to_book>")
		return sys.exit(1)
	print("============ BOOKBOT ============")
	print(sys.argv[1])

	details, words, chars =  get_book_text(sys.argv[1])
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	num_words = words
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	sorted_chars = sortChars(chars)
	for sorted_char in sorted_chars:
		if sorted_char['char'].isalpha():
			print(f"{sorted_char['char']}: {sorted_char['num']}")
	print("============= END ===============")


main()
