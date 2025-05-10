def get_book_text(filepath):
    with open(filepath) as file:
        # read the contents of the file
        book_text = file.read()
        # return the contents of the file
    return book_text


def count_words(book_text):
    num_words = len(book_text.split())
    return f"{num_words} total words"


def number_of_characters(book_text):
    # Create an empty dictionary to store character counts
    char_counts = {}

    # for-loop through each charachter in the book_text
    for char in book_text:
        char = char.lower()

        # Check if character is already in our dictonary
        if char in char_counts:
            char_counts[char] = char_counts[char] + 1
        else:
            char_counts[char] = 1

    return char_counts


def pretty_report(dictionary):
    pretty_list = []

    for char, count in dictionary.items():
        # Create a dictionary for this character
        char_dict = {"char": char, "num": count}
        # Add it to the list
        pretty_list.append(char_dict)

    # Define a function to extract the 'num' value for sorting
    def sort_on(dict_item):
        return dict_item["num"]

    # Sort the list in descending order based on the 'num' value
    pretty_list.sort(reverse=True, key=sort_on)

    return pretty_list
