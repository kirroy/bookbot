
from stats import get_num_words, get_num_single

count_dic = {}
def get_book_text(books_path):
    with open(books_path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    words = get_num_words(text)
    bstn = get_num_single(words)
    print(f"Number of words: {len(words)}")
    print(f"First word in lowercase: {bstn}")

main()
