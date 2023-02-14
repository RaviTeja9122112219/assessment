import re

def replace_words(text, word_dict):
    for key in word_dict:
        text = re.sub(r"\b" + key + r"\b", word_dict[key], text)
    return text

text = "This is a test string."
word_dict = {"test": "example", "string": "text"}

new_text = replace_words(text, word_dict)
print("Original text:", text)
print("Modified text:", new_text)
