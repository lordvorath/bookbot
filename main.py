def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)
    
def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    book = book.lower()
    chars = {}
    for c in book:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def get_file_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path):
    print(f"--- Begin report of {book_path} ---")
    file_contents = get_file_contents(book_path)
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")
    print()
    chars = count_characters(file_contents)
    for key in sorted(chars):
        if key.isalpha():
            print(f"The '{key}' character was found {chars[key]} times")
    print("--- End report ---")



main()