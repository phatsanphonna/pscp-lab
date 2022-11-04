'''
Week 13 - Roman
https://ejudge.it.kmitl.ac.th/problem/8347
'''

ROMAN_CHAR = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def main():
    '''Main Function'''

    roman_number = input()

    total = []

    for index, char in enumerate(roman_number):
        if index == 0:
            total.append(ROMAN_CHAR[char])
            continue

        if char == 'I':
            if roman_number[index + 1] != 'I':
                pop_char = total.pop()
                total.append(ROMAN_CHAR[pop_char] - 1)

        print(sum(total))


main()
