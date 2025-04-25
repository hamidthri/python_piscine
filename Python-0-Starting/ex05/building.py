# building.py
import sys


def analyze_text(text):
    """
    Analyzes the given text and counts the number of uppercase,
    lowercase, punctuation, spaces, and digits.

    Args:
        text: The string to analyze

    Returns:
        A tuple containing counts of uppercase, lowercase,
        punctuation, spaces, and digits
    """
    punctuation_str = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_count = sum(1 for char in text if char in punctuation_str)
    space_count = sum(1 for char in text if char.isspace())
    dig_count = sum(1 for char in text if char.isdigit())

    return upper_count, lower_count, punctuation_count, space_count, dig_count


def main():
    """
    Main function to run the text analysis.
    Usage: python building.py <text>
    """
    args = sys.argv[1:]

    try:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")

        if len(args) == 0:
            text = input("What is the text to count?\n")
        else:
            text = args[0]

        upper, lower, punct, space, digit = analyze_text(text)
        total = len(text)

        print(f"The text contains {total} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
