'''
Week 14 - PongYa
https://ejudge.it.kmitl.ac.th/problem/8392
'''


def main():
    '''Main Function'''

    number = input()

    if number[-1] == '3' or int(number) % 3 == 0:
        print('PONG')
    else:
        print(number)


main()
