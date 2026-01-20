#!/usr/bin/python3
"""
Print text with two new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'.

    Args:
        text: string to process

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    seps = {'.', '?', ':'}
    buffer = ""
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]
        buffer += ch
        if ch in seps:
            # Print segment followed by a blank line (2 newlines total)
            print(buffer.strip())
            print()
            buffer = ""
            i += 1
            # Skip spaces immediately after a separator
            while i < n and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Print any remaining text without trailing newline
    if buffer.strip() != "":
        print(buffer.strip(), end="")
