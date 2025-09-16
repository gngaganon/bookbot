import sys

# "If two strings are not passed after python3 is input into the terminal, the program ends"
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words

from stats import count_characters

from stats import sort_dictionaries

# sys.argv[1] takes <path_to_book> and inputs it into the following lines of code!
def main():
    number_of_each_character = count_characters(get_book_text(sys.argv[1]))
    dictionaries = sort_dictionaries(number_of_each_character)
    print(
        "============ BOOKBOT ============"
        f"\nAnalyzing book found at {sys.argv[1]}..."
        "\n----------- Word Count ----------"
        f"\nFound {count_words(get_book_text(sys.argv[1]))} total words"
        "\n--------- Character Count -------"
        )
    for dictionary in dictionaries:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")

main()