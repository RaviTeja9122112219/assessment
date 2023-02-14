import re

def is_anagram(str1, str2):
    # Remove white spaces and special characters
    str1 = re.sub(r'[^\w]', '', str1)
    str2 = re.sub(r'[^\w]', '', str2)

    # Convert to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Sort the strings
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    # Compare the sorted strings
    return str1 == str2

str1 = "This is a test string!"
str2 = "This is another test string!"

result = is_anagram(str1, str2)

if result:
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")
