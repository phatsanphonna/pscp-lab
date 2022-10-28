'''
Week 14 - Password
https://ejudge.it.kmitl.ac.th/problem/8374
'''

import hashlib


def main():
    '''Main Function'''

    password = input().encode('utf-8')

    hashed_password = hashlib.sha512(password).hexdigest()

    print(hashed_password.upper())


main()
