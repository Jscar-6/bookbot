import sys
from stats import get_num_words, get_char_count, get_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

word_count = get_num_words(filepath)
char_counts = get_char_count(filepath)
sorted_chars = get_sorted_list(char_counts)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")
        else: 
            continue

    print("============= END ===============")
    
main()
