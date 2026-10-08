# simple_utils.py - A tiny utility library

def reverse_string(text):
    """Reverses the characters in a string."""
    return text[::-1]

def count_words(sentence):
    """Count whitespace-separated words, ignoring leading and trailing whitespace.

    Consecutive whitespace counts as one separator. Empty or whitespace-only
    input returns zero.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """Convert a temperature in degrees Celsius to degrees Fahrenheit."""
    return (celsius * 9/5) + 32
