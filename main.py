from stats import get_word_count
from stats import count_characters

def get_book_text(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


def main():
    try:
        book_path = "books/frankenstein.txt"
        book_text = get_book_text(book_path)
    except:
        print("Failed to load book content.")

    if not book_text:
        print("Book content is empty.")
        return

    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document.")
    print(count_characters(book_text))
    
main()