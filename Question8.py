def is_valid_url(url):
    """
    Checks if the given string is a valid URL using basic string operations.
    :param url: The string to check.
    :return: True if valid, False otherwise.
    """
    # Check if it starts with "http://" or "https://"
    if url.startswith("http://") or url.startswith("https://"):
        # Remove "http://" or "https://"
        url = url.split("//")[1]

        # Check if there's a dot (.) in the remaining part
        if "." in url:
            # Ensure there's at least one character after the last dot
            if url.rsplit(".", 1)[-1]:
                return True

    return False  # If any check fails, return False

# Example usage:
print(is_valid_url("http://example.com"))  # True
print(is_valid_url("https://google.org"))  # True
print(is_valid_url("ftp://example.com"))   # False (doesn't start with http/https)
print(is_valid_url("http://example"))      # False (no dot)
print(is_valid_url("http://example."))     # False (no characters after dot)
