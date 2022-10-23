'''Week 12 - MissingCard I'''


def main():
    '''Main Function'''

    rank = [
        'A', 'K', 'Q', 'J', '10',
        '9', '8', '7', '6', '5',
        '4', '3', '2'
    ]
    suffix = ['S', 'H', 'D', 'C']

    deck = []

    for suf in suffix:
        for ran in rank:
            deck.append(ran + suf)

    for _ in range(51):
        card = input().upper()
        deck.remove(card)

    print(*deck, sep='')


main()
