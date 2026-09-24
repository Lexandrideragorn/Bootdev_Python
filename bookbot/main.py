from stats import countWords, getBookText, characterCount
from stats import chars_dict_to_sorted_list as cDicttoSlist
from sys import argv,exit

def main():
    if len(argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_path=argv[1]
    bookFrankenstein = getBookText(book_path) 
    word_count = countWords(bookFrankenstein)
    characters = characterCount(bookFrankenstein)
    chars_sorted_list=cDicttoSlist(characters)
    #print( f"{num_words} words found in the document") 
    #print(f"Found {num_words} total words")
    #for l in chars_sorted_list:
    #    print(f"'('{l[0]}', {l[1]})'")
    print_report(book_path,word_count,chars_sorted_list)

def print_report(path, count, sList):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for l in sList:
        if str.isalpha(l[0]): print(f"{l[0]}: {l[1]}")
    print("============= END ===============")


#book_path="books/frankenstein.txt"

main()
