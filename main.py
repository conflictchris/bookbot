from stats import count_words
from stats import count_characters

# This is the main file for the bookbot

#Write a function call 'get_book_text'.  It takes a filepath as input and reutrns the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
   
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    num_char = count_characters(book_text)
    print(f"{num_words} words found in the document")
    print(num_char)

main()