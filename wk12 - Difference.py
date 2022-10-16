'''
Week 12 - Difference
https://ejudge.it.kmitl.ac.th/problem/8324
'''


def main():
    '''Main Function'''

    total_a_member = int(input())
    total_b_member = int(input())

    set_a = set()
    set_b = set()

    for _ in range(total_a_member):
        number = int(input())

        set_a.add(number)

    for _ in range(total_b_member):
        number = int(input())

        set_b.add(number)

    diff = sorted(set_a.difference(set_b))

    print(*diff, sep=' ')


main()
