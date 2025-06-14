from stats import count_words, count_characters, sort_dictionary
import sys
import textwrap

def get_book_text(fpath):

    with open(fpath) as f:
        contents = f.read()

    return contents

def main():

    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)    
    num_words = count_words(book_text)
    character_dictionary = count_characters(book_text)
    sorted_dictionary = sort_dictionary(character_dictionary)
    
    print(textwrap.dedent(f"""
    ============ BOOKBOT ============
    Analyzing book found at {path_to_book}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------"""))

    for item in sorted_dictionary:
        if item["name"].isalpha():
            print(f"{item['name']}: {item['num']}")

main()