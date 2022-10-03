'''Week 3 - [Pre] Blackjack.py'''


def main():
    '''Main Function'''

    total_score = 0
    have_ace = 0

    total_cards = int(input())

    for _ in range(total_cards):
        card = input()

        if card.upper() in 'JKQ':
            total_score += 10
        elif card.upper() == 'A':
            total_score += 11
            have_ace += 1
        else:
            total_score += int(card)

    if not have_ace:
        print(total_score)
        return

    for _ in range(have_ace):
        if total_score > 21:
            total_score -= 10

    print(total_score)


main()
