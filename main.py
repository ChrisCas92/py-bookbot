# The code below is an example of how to use the with statement in Python

# a with block is a context manager that used to open a file
# and automatically closes the file after the block is executed, cleaning up resources
with open("books/frankenstein.txt") as f:
    # read the contents of the file f
    # and store it in a variable called file_contents
    file_contents = f.read()


def get_book_text(filepath):
    with open(filepath) as file:
        # read the contents of the file
        book_text = file.read()
        # return the contents of the file
    return book_text

    # accepts the text from the book as a string, and returns the number
    # of words in the string


filepath = ""


def count_words(book_text):
    num_words = len(book_text.split())
    return f"{num_words} words found in the document"


def main():
    # call the function get_book_text with the path to the file frankenstein.txt
    # print(get_book_text("books/frankenstein.txt"))

    print(count_words(get_book_text("books/frankenstein.txt")))


# call the main function
main()
