from typing import Optional

"""
Find the longest word in a string
"""


def get_token(s: str, i: int) -> (str, int):
    """
    This function takes a string a location in the string and returns the next token in the string and the location of the next token in the string.
    """

    # Skip leading spaces
    while i < len(s) and s[i] == ' ':
        i += 1

    # Find the start of the token
    start = i
    while i < len(s) and s[i] != ' ':
        i += 1

    # Return the token and the location of the next token

    return s[start:i], i


def longest_word(s: str) -> Optional[str]:
    """
    This function takes a string and returns the longest word in the string.
    """

    if len(s) == 0:
        return None

    longest = ""
    i = 0
    while i < len(s):
        token, i = get_token(s, i)
        if len(token) > len(longest):
            longest = token
    return longest


if __name__ == "__main__":
    print(longest_word("This is a test")) # This
    print(longest_word("This is a longer test")) # longer
    print(longest_word("This is the longest test")) # longest
