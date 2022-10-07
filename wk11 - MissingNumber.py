'''
Week 11 - MissingNumber
https://ejudge.it.kmitl.ac.th/problem/8281
'''


def main():
    '''Main Function'''

    n_value = int(input())

    number_list = []

    while True:
        number = int(input())

        if number == 0:
            break

        number_list.append(number)

    for i in range(1, n_value+1):
        if i not in number_list:
            print(i)


main()
