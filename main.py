def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print(f"the number of words is: {get_amount(text)}")

    #print(text)

def get_amount(text):
    amount = text.split()
    return len(amount)
    

def get_book_path(path):
    with open(path) as f:
        return f.read()
main()