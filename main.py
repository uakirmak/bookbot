from stats import get_word_count

with open('/Users/umitakirmak/Desktop/StudyProjects/BootDev/workspace/github.com/uakirmak/bookbot/books/frankenstein.txt', 'r') as file:
    file_contents = file.read()
    # print(file_contents)


print(get_word_count(file_contents))
