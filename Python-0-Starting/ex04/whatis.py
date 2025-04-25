import sys


def main():
    """
    Check if the given number is odd or even.
    Usage: python whatis.py <integer>
    """
    args = sys.argv[1:]

    try:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")

        if len(args) == 0:
            return

        num = int(args[0])
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
