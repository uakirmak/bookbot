def get_word_count(text):
    clean_text = text.split()
    count = 0
    for word in clean_text:
        count += 1
    # print(clean_text)
    return f"{count} words found in the document"


def get_char_count(text):
    my_dict = {}
    for char in text:
        formatted_char = char.lower()
        my_dict[formatted_char] = my_dict.get(formatted_char, 0) + 1
    return my_dict
