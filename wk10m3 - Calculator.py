'''
Midterm 4 - Calculator
Week 10 - Calculator
https://ejudge.it.kmitl.ac.th/problem/8271
'''


def main():
    '''Main Function'''

    n_value = int(input())

    total_press = 0

    if n_value == 1:
        print(1)
        return

    for i in range(1, n_value+1):
        total_press += len(str(i)) + 1

    print(total_press)


main()
