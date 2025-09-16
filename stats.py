def count_words(book):
    words = book.split()
    count = len(words)
    return count
# book is a string version of a filepath, count is an integer

def count_characters(book):
    book_characters = list(book)
    unique_characters = set(book_characters)
    counters = {}
    for character in book_characters:
        if character.lower() in unique_characters and character.lower() in counters:
            counters[character.lower()] += 1
        else:
            counters[character.lower()] = 1
    return counters

def sort_on(dictionary):
    return dictionary["num"]

def sort_dictionaries(dictionary):
    key_value_pairs = []
    characters_counts = dictionary
    for character, count in characters_counts.items():
        key_value_pairs.append({"char": character, "num": count})
    key_value_pairs.sort(reverse=True, key=sort_on)
    return key_value_pairs