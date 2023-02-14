import re

def capitalize_sentences(text):
    # Split the text into sentences using regular expressions
    sentences = re.split(r'(?<=[.!?]) +', text)
    
    # Capitalize the first letter of each sentence
    capitalized_sentences = [sentence[0].upper() + sentence[1:] for sentence in sentences]
    
    # Join the sentences back into a single string
    capitalized_text = ' '.join(capitalized_sentences)
    
    return capitalized_text

text = "this is the first sentence. this is the second sentence."
print(capitalize_sentences(text))
