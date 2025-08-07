from stats import get_num_words
from stats import get_chararacter_counts
from stats import get_sorted_dictionary

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    
    

    
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    counts = get_chararacter_counts(text)
    sorted = get_sorted_dictionary(counts)

    for i in range(0, len(sorted)):
        if (sorted[i]["char"].isalpha()):
            print(f"{sorted[i]["char"]}: {sorted[i]["num"]}")
        

    print("============= END ===============")

main()