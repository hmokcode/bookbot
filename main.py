def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    lowered_text = lower_case(text)
    split_string = split_char(lowered_text)
    counted_chars = count_char(split_string)
    converted = convert_dictionary(counted_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{get_amount(text)} words found in the document \n")
    converted.sort(reverse=True, key=sort_on)
    for sort in converted:
        print(f"The character '{sort["char"]}' was found {sort["amount"]} times")
    print("--- End report ---")
    #print(sort)
    #print(split_string)
    #print(lowered_text)
    #print(text)

def sort_on(converted):
    return converted["amount"]

def convert_dictionary(counted_chars):
    list_of_dict = []
    for  chari, counti in counted_chars.items():
        new_dict = {"char": chari, "amount": counti}
        list_of_dict.append(new_dict)
    return list_of_dict


def count_char(split_string):
    alphabet_count = {}
    for char in split_string:
        if char.isalpha():
            if char in alphabet_count:
                alphabet_count[char] += 1
            else:
                alphabet_count[char] = 1
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