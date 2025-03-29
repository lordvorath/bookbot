from stats import count_words, count_chars, sort_dicts

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    txt = get_book_text("books/frankenstein.txt")
    count = count_words(txt)
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    chars = count_chars(txt)
    print ("--------- Character Count -------")
    lst = sort_dicts(chars)
    for i in lst:
        if not i['key'].isalpha():
            continue
        print(f"{i['key']}: {i['val']}")
    print("============= END ===============")

main()