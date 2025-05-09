# Write a function that accepts the text from the book as a string and returns the number of words in the string    

def count_words(string):
    words = string.split()
    num_words = len(words)
    return num_words