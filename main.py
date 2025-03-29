from stats import count_words

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    txt = get_book_text("books/frankenstein.txt")
    count = count_words(txt)
    print(f"{count} words found in the document")

main()