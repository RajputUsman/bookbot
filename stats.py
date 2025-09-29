def words_in_book(bookinfo):
	words_list = bookinfo.split()
    
	chars = chars_in_book(words_list)
	return len(words_list), chars

def chars_in_book(words):
    details = {}
    for word in words:
        for char in word:
            if char.lower() not in details:
                details[char.lower()] = 0
            details[char.lower()] += 1

    return details 


def sort_on(items):
     return items["num"]

def sortChars(dictOfchars):
    charlist = []
    for char in dictOfchars:
        charlist.append({"char": char,"num": dictOfchars[char]})
    charlist.sort(reverse=True,key=sort_on)
    return charlist