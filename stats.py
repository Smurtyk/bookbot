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


def sort_dict(d):
    sorted_items = list(d.items())
    sorted_items = sorted(sorted_items, key=lambda item: item[1], reverse=True)
    return dict(sorted_items)
