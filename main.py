def get_book_text():
    filepath = "books/frankenstein.txt"
    return filepath

def print_text():
    filepath = get_book_text()
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    num_words = 0
    book_contents = print_text()
    for word in book_contents.split():
        num_words += 1
    print(f"{num_words} words found in the document")

main()