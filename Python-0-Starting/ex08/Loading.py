# Loading.py
import sys


def ft_tqdm(lst: range) -> None:
    """
    A simplified implementation of tqdm progress bar.

    Args:
        lst: A range object to iterate through

    Yields:
        Each element in the range
    """
    total = len(lst)
    bar_length = 60

    for i, item in enumerate(lst, 1):
        progress = int(100 * i / total)
        filled_length = int(bar_length * i / total)
        bar = "█" * filled_length + " " * (bar_length - filled_length)

        sys.stdout.write("\r")
        sys.stdout.write(f"{progress:3d}%|{bar}| {i}/{total}")
        sys.stdout.flush()

        yield item

    print()
