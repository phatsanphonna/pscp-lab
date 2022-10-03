'''
[Recommend]
Week 6 - RockPaperScissor
'''


def check_winner(p1_action: str, p2_action: str):
    '''
    Check who is winner

    If player 1 wins will return 1,
    Else if player 2 wins will return 2,
    Else if draws will return 999
    '''

    if p1_action == p2_action:
        return 999

    if p1_action == 'R':
        if p2_action == 'S':
            return 1
        elif p2_action == 'P':
            return 2
    elif p1_action == 'P':
        if p2_action == 'S':
            return 2
        elif p2_action == 'R':
            return 1
    elif p1_action == 'S':
        if p2_action == 'R':
            return 2
        elif p2_action == 'P':
            return 1


def main():
    '''Main Function'''

    sequence = input()

    player1_action = None
    player2_action = None

    player1_wins = 0
    player2_wins = 0

    for action in sequence:
        if not player1_action:
            player1_action = action
            continue

        player2_action = action

        result = check_winner(player1_action, player2_action)

        if result == 1:
            player1_wins += 1
        elif result == 2:
            player2_wins += 1
        elif result == 999:
            pass

        player1_action = None
        player2_action = None

    if player1_wins == player2_wins:
        print('DRAW %d' % player1_wins)
    elif player1_wins > player2_wins:
        print('A win %d-%d' % (player1_wins, player2_wins))
    elif player1_wins < player2_wins:
        print('B win %d-%d' % (player2_wins, player1_wins))


main()
