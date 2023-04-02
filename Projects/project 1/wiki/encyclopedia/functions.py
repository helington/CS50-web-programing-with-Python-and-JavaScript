from random import randint
from markdown2 import Markdown


def compare_string(string, strings):
    verification = False
    new_string = ''
    for i in range(len(strings)):
        print(strings[i])
        if strings[i].lower() == string.lower():
            new_string = strings[i]
            verification = True
    return verification, new_string

def random_page(entries):
    random_page = entries[randint(0, len(entries) - 1)]
    return random_page


def convert_markdown_to_html(markdon_content):
    markdowner = Markdown()
    converted_page = markdowner.convert(markdon_content)
    return converted_page

