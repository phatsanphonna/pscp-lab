'''Week 3 - [Pre] Blackjack.py'''


def main():
    '''Main Function'''

    cards = []
    have_ace = 0

    total_cards = int(input())

    for _ in range(total_cards):
        card = input()

        if card.upper() == 'J' or card.upper() == 'K' or card.upper() == 'Q':
            cards.append(10)
        elif card.upper() == 'A':
            cards.append(11)
            have_ace += 1
        else:
            cards.append(int(card))

    total_score = sum(cards)

    if not have_ace:
        print(total_score)
        return

    for _ in range(have_ace):
        if total_score > 21:
            total_score -= 10

    print(total_score)


main()
