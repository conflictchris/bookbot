# This is the main file for the bookbot

#Write a function call 'get_book_text'.  It takes a filepath as input and reutrns the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# Write a function that accepts the text from the book as a string and returns the number of words in the string    
def count_words(string):
    words = string.split()
    num_words = len(words)
    return num_words
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

main()