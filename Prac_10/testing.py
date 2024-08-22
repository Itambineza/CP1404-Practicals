"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("the quick brown fox jumps over the lazy dog")
    'The quick brown fox jumps over the lazy dog.'
    """
    if phrase:
        return phrase[0].upper() + phrase[1:].rstrip(".") + "."
    else:
        return ""


def run_tests():
    """Run the tests on the functions."""
    # Assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Assert test with custom message, used to see if Car's init method sets the odometer correctly
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Assert tests to check if Car sets the fuel correctly
    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when passing a value"
    car = Car()
    assert car.fuel == 0, "Car does not set fuel correctly using the default value"

    # Run doctests
    doctest.testmod()


if __name__ == '__main__':
    run_tests()