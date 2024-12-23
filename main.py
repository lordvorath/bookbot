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

def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_file_contents(book_path)
    word_count = count_words(file_contents)
    print(word_count)
    char_count = count_characters(file_contents)
    print(char_count)

main()