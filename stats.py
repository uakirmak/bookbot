def get_word_count(text):
    clean_text = text.split()
    count = 0
    for word in clean_text:
        count += 1
    print(clean_text)
    return clean_text
