# This is the main file for the bookbot

#Write a function call 'get_book_text'.  It takes a filepath as input and reutrns the contents of the file as a string
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)
    
main()