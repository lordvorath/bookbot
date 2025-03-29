def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(txt):
    return len(txt.split())

def main():
    txt = get_book_text("books/frankenstein.txt")
    count = count_words(txt)
    print(f"{count} words found in the document")

main()