import sys
from ft_filter import ft_filter


def main():
    """
    Filters words in a string that have length greater than N.

    Usage: python filterstring.py <string> <integer>
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        S = sys.argv[1]
        N = int(sys.argv[2])

        if not isinstance(S, str):
            raise AssertionError("the arguments are bad")

        if N < 0:
            raise AssertionError("the arguments are bad")

        words = S.split()
        result = list(ft_filter(lambda word: len(word) > N, words))

        print(result)

    except ValueError:
        print("AssertionError: the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
