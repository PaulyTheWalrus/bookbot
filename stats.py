filepath = "books/frankenstein.txt"

def get_book_text():
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    num_words = 0
    book_contents = get_book_text()
    for word in book_contents.split():
        num_words += 1
    print(f"{num_words} words found in the document")