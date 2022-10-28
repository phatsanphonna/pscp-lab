'''
Week 13 - SMS
https://ejudge.it.kmitl.ac.th/problem/8355
'''

_SEQUENCE = {
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}


def main():
    '''Main Function'''

    loops = int(input())

    message = ''

    for _ in range(loops):
        press = int(input())
        press_sequence = int(input())

        if press == 1:
            message = message[:-press_sequence]
            continue

        if str(press) in '79':
            char = press_sequence % 4
            message += _SEQUENCE[press][char-1]
        elif str(press) in '234568':
            char = press_sequence % 3
            message += _SEQUENCE[press][char-1]

    if not message:
        print('null')
        return

    print(message)


main()
