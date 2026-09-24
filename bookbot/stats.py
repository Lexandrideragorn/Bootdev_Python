
def getBookText(filepath):
    with open(filepath) as f:
        contents = f.read()
        return(contents)

def countWords(book):
    return len(book.split())

def characterCount(book) -> dict[str,int]:
    count = {}
    for l in book.lower():
        count[l] = count.get(l,0) +1

    return count

def sort_on(book: tuple[str,int]) -> int:
    return book[1]

def chars_dict_to_sorted_list(book: dict[str,int]):
    sorted_list =[]
    for l,c in book.items():
        sorted_list.append((l,c))
    return sorted(sorted_list, reverse=True, key=sort_on)


    
