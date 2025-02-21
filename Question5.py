def find_pattern(text):
    """
    Finds occurrences of words that start with 'b', contain any number of letters, and end with 'Bob'.

    :param text: The input string to search for patterns.
    :return: The count of matches found.
    """
    words = text.split()  # Split the text into words
    count = 0  # Counter for matches

    for word in words:
        if word.startswith('b') and word.endswith('Bob'):  # Check pattern
            count += 1

    return count  # Return the number of matches


# Example usage:
text = "bHelloBob bobby bCoolBob b123Bob bBob"
print(find_pattern(text))  # Output: 3
