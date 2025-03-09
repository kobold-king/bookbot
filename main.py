from stats import (
    get_word_count,
    list_dict,
    get_character_count,
)
import sys

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    character_list = list_dict(character_count)
    print_report(book_path, word_count, character_list)

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, word_count, character_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in character_list:
        if not item["letters"].isalpha():
            continue
        print(f"{item['letters']}: {item['num']}")

    print("============= END ===============")

main()
