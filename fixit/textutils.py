"""Small text helpers."""


def is_palindrome(text: str) -> bool:
    """Check whether text reads the same forwards and backwards.

    Example:
        is_palindrome("madam") returns True.
        is_palindrome("hello") returns False.
    """

    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def reverse_words(text: str) -> str:
    """Reverse the order of words in text.

    Example:
        reverse_words("hello world") returns "world hello".
    """
    return " ".join(reversed(text.split()))


def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug.

    Example:
        slugify("Hello World!") returns "hello-world".
    """
    import re

    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")

def convert_case(style: str, text: str) -> str:
    """Convert text into the specified naming convention.

    Supported styles:
        snake: hello_world
        kebab: hello-world
        camel: helloWorld
        pascal: HelloWorld
    """
    valid_styles = {"snake", "kebab", "camel", "pascal"}

    if style not in valid_styles:
        raise ValueError(f"Unsupported style: {style}")

    words = text.replace("-", " ").replace("_", " ").split()
    words = [word.lower() for word in words]

    if style == "snake":
        return "_".join(words)

    if style == "kebab":
        return "-".join(words)

    if style == "camel":
        return words[0] + "".join(word.capitalize() for word in words[1:]) if words else ""

    if style == "pascal":
        return "".join(word.capitalize() for word in words)

    return ""
