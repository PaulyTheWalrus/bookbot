from stats import sort_dict, get_num_letters, get_num_words, filepath

def main():
    report = sort_dict(get_num_letters())
    num_words = get_num_words()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for small_dict in report:
        if small_dict["char"].isalpha():
            print(f"{small_dict['char']}: {small_dict['num']}")

main()