def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count


def count_characters(text):
    char_counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts