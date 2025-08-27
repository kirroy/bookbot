
import sys
from stats import get_num_single, get_num_words, sorting, dics_list, dic_einzel
count_dic = {}
zahl = 0
def get_book_text(books_path):
    with open(books_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    words = get_num_words(text)
    dic = get_num_single(text)
    liste = dics_list(dic)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {len(words)} total words")
    print("----------- Character Count -----------")
    dic_einzel(liste)
    print("============= END ===============")
main()
