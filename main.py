from stats import get_book_text, count_words, number_of_characters, pretty_report
import sys

# The code below is an example of how to use the with statement in Python

# a with block is a context manager that used to open a file
# and automatically closes the file after the block is executed, cleaning up resources
# with open(sys.argv) as f:
# read the contents of the file f
# and store it in a variable called file_contents
#   file_contents = f.read()


def main():
    # Check if the user provided a file path as a command line argument
    if len(sys.argv) > 1:
        # If so, use the provided file path
        file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        print("Please provide the path to the book file.")
        sys.exit(1)

    book_text = get_book_text(file_path)

    # Count words and characters
    word_count = count_words(book_text)
    character_counts = number_of_characters(book_text)

    # Get sorted character counts
    sorted_chars = pretty_report(character_counts)

    # call the function get_book_text with the path to the file frankenstein.txt
    # print(get_book_text("books/frankenstein.txt"))

    # print(count_words(get_book_text("books/frankenstein.txt")))

    # print(number_of_characters(get_book_text("books/frankenstein.txt")))

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count}")
    print("--------- Character Count -------")

    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        # Check if the character is alphabetic
        if char.isalpha():
            count = char_dict["num"]
            print(f"{char}: {count}")

    print("============= END ===============")


# call the main function
main()
