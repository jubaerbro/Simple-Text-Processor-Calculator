# text_tools.py

def shout(text):
    """Converts a string to uppercase and adds an exclamation mark."""
    return text.upper() + "!"

def reverse_string(text):
    """Reverses the characters in a string."""
    return text[::-1]

def count_words(text):
    """Counts the number of words in a string."""
    return len(text.split())
