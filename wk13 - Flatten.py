'''
Week 13 - Flatten
https://ejudge.it.kmitl.ac.th/problem/8343
'''


def main():
    '''Main Function'''

    sequence = input()

    number_list = []

    number_holder = ''

    for char in sequence:
        if char.isnumeric() or char == '-':
            number_holder += char
            continue

        if number_holder:
            number_list.append(int(number_holder))
            number_holder = ''

    number_list.sort(reverse=True)

    print(number_list)


main()
