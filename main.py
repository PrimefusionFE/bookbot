def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def get_num_words(str):
    str_split = str.split()
    return len(str_split)

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

main()