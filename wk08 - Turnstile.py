'''
Week 8 - Turnstile
https://ejudge.it.kmitl.ac.th/problem/8241
'''


def main():
    '''Main Function'''

    is_locked = True
    count = 0

    while True:
        state = input()

        if state == 'END':
            break

        if state == 'P' and is_locked:
            continue
        elif state == 'P' and not is_locked:
            count += 1
            is_locked = True
        elif state == 'C' and is_locked:
            is_locked = False
        elif state == 'C' and not is_locked:
            continue

    print(count)


main()
