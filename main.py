import string
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    lowered_text = lower_case(text)
    split_string = split_char(lowered_text)
    count = count_char(split_string)
    
    print(count)
    #print(split_string)
    #print(lowered_text)
    #print(f"the number of words is: {get_amount(text)}")
    #print(text)

def count_char(split_string):
    alphabet = list(string.ascii_lowercase)
    alphabet_count = []
    for char in alphabet:
        number = 0
        for char_split in split_string:
            if char == char_split:
                number += 1
        alphabet_count.append(f"{char}: {number}")
    return alphabet_count

def split_char(lowered_text):
    char_string = list(lowered_text)
    return char_string

def lower_case(text):
    lowered_string = text.lower()
    return lowered_string

def get_amount(text):
    amount = text.split()
    return len(amount)

def get_book_path(path):
    with open(path) as f:
        return f.read()
main()