def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print(f"the number of words is: {get_amount(text)}")
    lowered_text = lower_case(text)
    split_string = split_char(lowered_text)

    print(split_string)
    #print(lowered_text)
    #print(text)


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