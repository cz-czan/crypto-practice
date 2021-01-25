import string
low_case = string.ascii_lowercase
upper_case = string.ascii_uppercase

low_case += low_case
upper_case += upper_case

def e(num, plaintext):
    ciphertext = ""
    for char in plaintext:
        if char in low_case:
            char = low_case[low_case.index(char) + num]
            ciphertext += char
        elif char in upper_case:
            char = upper_case[upper_case.index(char) + num]
            ciphertext += char


    return ciphertext

def d(num, ciphertext):
    plaintext = ""
    for char in ciphertext:
        if char in low_case:
            char = low_case[low_case.index(char) - num]
            plaintext += char
        elif char in upper_case:
            char = upper_case[upper_case.index(char) - num]
            plaintext += char

    return plaintext
