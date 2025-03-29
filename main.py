from stats import count_words, count_chars, sort_dicts
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    txt = get_book_text(path)
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