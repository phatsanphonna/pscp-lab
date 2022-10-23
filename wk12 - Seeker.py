'''
Week 12 - Seeker
https://ejudge.it.kmitl.ac.th/problem/8329
'''


def main():
    '''Main Function'''

    text = input()

    number_holder = '0'
    number_list = []

    for char in text:
        if char.isnumeric():
            number_holder += char
            continue

        number_list.append(int(number_holder))
        number_holder = '0'

    if number_holder.isnumeric():
        number_list.append(int(number_holder))
        number_holder = '0'

    print(sum(number_list))


main()
