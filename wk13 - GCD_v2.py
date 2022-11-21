'''
Week 12 - GCD_v2
https://ejudge.it.kmitl.ac.th/problem/8335
'''


def find_gcd(div: int, mod: int):
    '''Find GCD'''

    if mod == 0:
        return div

    return find_gcd(mod, div % mod)


def main():
    '''Main Function'''

    num_1 = int(input())
    num_2 = int(input())

    gcd = find_gcd(num_1, num_2)

    print(gcd)


main()
