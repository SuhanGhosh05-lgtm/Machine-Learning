def word_count(text: str) -> int:
    """
    Return the number of words in `text`, where words are
    separated by any run of whitespace. Leading and trailing
    whitespace does not create extra words.
    """
    return len(text.split())
    pass


def reverse_word_order(text: str) -> str:
    """
    Split `text` on whitespace, reverse the order of the words
    (a list can be sliced with [::-1] like a string), and
    return them joined by single spaces.

    Example: reverse_word_order("  one  two three ") -> "three two one"
    """
    words = text.split()
    words = words[::-1]
    return " ".join(words)
    pass


def last_field(line: str, sep: str) -> str:
    """
    Return the text after the LAST occurrence of `sep` in
    `line`. If `sep` does not occur, return `line` unchanged.
    Use rsplit() with a maxsplit of 1 and the index -1.

    Example: last_field("a/b/c.txt", "/") -> "c.txt"
    """
    return line.rsplit(sep, 1)[-1] if sep in line else line
    pass


def count_nonblank_lines(text: str) -> int:
    """
    Return how many lines in `text` (as split by splitlines())
    contain at least one character that is not whitespace.
    """
    lines = text.splitlines()
    count = 0

    for line in lines:
        if line.strip():
            count += 1

    return count
    pass


def make_csv_line(fields) -> str:
    """
    `fields` is a list of strings. Return one string in which
    the fields are joined by ",". Any field that contains a
    comma is first wrapped in double quotes.

    Example: make_csv_line(["a", "b,c", "d"]) -> 'a,"b,c",d'
    """
    result = []
    for field in fields:
        if "," in field:
            field = '"' + field + '"'
        result.append(field)
    return ",".join(result)
    pass
