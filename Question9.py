def days_since_birth(birthday):
    """
    Calculates the number of days passed since birth, excluding the birth year and the current year.
    :param birthday: Birthdate in "DD-MM-YYYY" format (string)
    :return: Number of days (integer)
    """
    # Step 1: Extract the birth year from the string
    birth_year = int(birthday.split("-")[2])

    # Step 2: Define the current year (since we can't use imports)
    current_year = 2025

    # Step 3: Compute the number of whole years passed (excluding birth and current year)
    whole_years = (current_year - birth_year) - 2

    # Step 4: Convert years to days
    total_days = whole_years * 365

    return total_days

# Example usage:
print(days_since_birth("20-12-2005"))  # Output: (2025 - 2005 - 2) * 365 = 6570
