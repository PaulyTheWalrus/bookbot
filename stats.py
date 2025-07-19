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
    return num_words

def get_num_letters():
    letter_dict = {}
    book_contents = get_book_text()
    for letters in book_contents.lower():
        if letters in letter_dict:
            letter_dict[letters] += 1
        else:
            letter_dict[letters] = 1
    return letter_dict

def sort_dict(keys):
    new_sorted_dict = []
    for key in keys:
        small_dict = {"char": key, "num": keys[key]}
        new_sorted_dict.append(small_dict)
    new_sorted_dict.sort(key=sort_on, reverse=True)
    return new_sorted_dict

def sort_on(items):
    return items["num"]