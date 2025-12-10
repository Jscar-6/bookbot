contents = ""

def get_num_words(filepath):
    a = read_and_split(filepath)
    return len(a)

def read_and_split(filepath):
    with open(filepath) as f:
        contents = f.read()
        contents = contents.lower()
        contents = contents.split()
    return contents

def read_and_lower(filepath):
    with open(filepath) as f:
        rtext = f.read()
        rtext = rtext.lower()
    return rtext

def get_char_count(filepath):
    char_count_dict = {}
    a = read_and_lower(filepath)
    for char in a:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict
