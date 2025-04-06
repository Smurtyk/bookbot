from stats import get_word_count
from stats import count_characters
from stats import sort_dict
import sys

def get_book_text(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return ""


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    if not book_text:
        print("Failed to load book content.")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_counts = count_characters(book_text)
    sorted = sort_dict(char_counts)
    for char in sorted:
        print(f"{char}: {char_counts[char]}")
    print("--------- Character Count -------")
    
main()
