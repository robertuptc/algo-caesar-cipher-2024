def caesar_cipher(string, shift_amount):
    list_of_str = list(string)
    return shifting(list_of_str, shift_amount)


def shifting(list_str, shift_amount):
    answer = ""
    for letter in list_str:
        if letter == " ":
            answer += " "
        elif not letter.isalpha():
            answer += letter
        elif letter.isupper():
            if ord(letter) + shift_amount > 90:
                answer += wrapping(letter, shift_amount, 90, 64)
            elif ord(letter) + shift_amount < 65:
                answer += wrapping(letter, shift_amount, 64, 90)
            else:
                answer += chr(ord(letter) + shift_amount)
        else:
            if ord(letter) + shift_amount > 122:
                answer += wrapping(letter, shift_amount, 122, 96)
            elif ord(letter) + shift_amount < 97:
                answer += wrapping(letter, shift_amount, 96, 122)
            else:
                answer += chr(ord(letter) + shift_amount)
    return answer

def wrapping(l, shift, max_num, a_A_charcode):
    answer = ""
    wrap = shift - (max_num - ord(l)) 
    answer += chr(a_A_charcode + wrap)
    return answer