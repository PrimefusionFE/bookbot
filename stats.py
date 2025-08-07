def get_num_words(str):
    str_split = str.split()
    return len(str_split)

def get_chararacter_counts(str):
    d = {}
    i = 0
    for char in str:
        lower = char.lower()
        if lower in d:
            d[lower] = d[lower] + 1
        else:
            d[lower] = 1

    return d