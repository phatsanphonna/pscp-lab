'''
[Recommend]
Week 7 - [Pre week 3] Hamburger.py
'''


def main():
    '''Main Function'''

    left_bun = int(input())
    right_bun = int(input())

    meats = (left_bun + right_bun) * 2

    print(('|'*left_bun) + ('*'*meats) + ('|'*right_bun))


main()
