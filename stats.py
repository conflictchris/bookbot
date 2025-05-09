"""
Write a function that accepts the text from the books as a string and returns the number of words in the string

"""   

def count_words(string):
    words = string.split()
    num_words = len(words)
    return num_words
"""
Write a function that taskes the text from the book as a string,
returns the number of times each character(inc symbols and spaces) appears

    convert any character to lowercase 
    Use a dictionary of String -> Integer
    {'p': 6121, 'r': 20818, 'o': 25225, ...}
    
"""

def count_characters(string):
    dict_chars = {}
    string = string.lower()
    for char in string:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1
    return dict_chars