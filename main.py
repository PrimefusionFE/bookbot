from stats import get_num_words
from stats import get_chararacter_counts

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    counts = get_chararacter_counts(text)
    print(counts)

main()