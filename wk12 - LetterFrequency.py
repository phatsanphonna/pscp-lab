'''
Week 12 -LetterFrequency
https://ejudge.it.kmitl.ac.th/problem/8327
'''


def main():
    '''Main Function'''

    sentence = input()

    char_list = {}

    for char in sentence:
        if not char.isalpha():
            continue

        char = char.lower()

        if char_list.get(char):
            char_list[char] += 1
        else:
            char_list[char] = 1

    most_used_total = float('-inf')
    most_used_char = ''

    for key in char_list:
        if char_list[key] > most_used_total:
            most_used_total = char_list[key]
            most_used_char = key

    print(most_used_char)


main()
