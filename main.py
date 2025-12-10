from stats import get_num_words, get_char_count

def main():
    path = "books/frankenstein.txt"
    print(f"Found {get_num_words(path)} total words")
    print(get_char_count(path))

main()
