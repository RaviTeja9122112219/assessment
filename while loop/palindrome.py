def palindrome(s):
    min = 0
    max = len(s) - 1
    while min < max:
        if s[min] != s[max]:
            return False
        min  = min + 1
        max = max - 1
    return True

result = palindrome("aba")
print(result)
