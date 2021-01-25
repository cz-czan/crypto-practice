import string


def char_to_num(char :string):
    low_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase

    if char in low_case:
        return low_case.index(char)
    if char in upper_case:
        return upper_case.index(char)

def num_to_char(num :int):
    upper_case = string.ascii_uppercase
    if num > len(upper_case) - 1:
        num -= len(upper_case)
    return upper_case[num]



def e(key, plaintext):
    plaintext =  plaintext.replace(" ", "")
    while len(key) < len(plaintext):
        key += key
    if len(key) > len(plaintext):
        key = key[:len(plaintext)]
    ciphertext = ""
    for i in range(0, len(plaintext)):
        pc_i = char_to_num(plaintext[i]) # plaintext char index
        kc_i = char_to_num(key[i]) # key char index
        ciphertext += num_to_char(pc_i+kc_i)

    return ciphertext

def d(key, ciphertext):
    ciphertext = ciphertext.replace(" ", "")
    while len(key) < len(ciphertext):
        key += key
    if len(key) > len(ciphertext):
        key = key[:len(ciphertext)]
    plaintext = ""
    for i in range(0, len(ciphertext)):
        cc_i = char_to_num(ciphertext[i]) # ciphertext char index
        kc_i = char_to_num(key[i]) # key char index
        plaintext += num_to_char(cc_i - kc_i)

    return plaintext