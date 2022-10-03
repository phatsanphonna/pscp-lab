'''
Midterm 6 - Volleyball
Week 10 - Volleyball
'''

DEAL_SCORE = 24
WIN_SCORE = 25

LAST_SET = 5
LAST_SET_DEAL_SCORE = 14
LAST_SET_WIN_SCORE = 15

WIN_SET = 3


def display_win_message(team: str, lose_set: int):
    '''Display win message'''

    print('%s won 3:%d set' % (team, lose_set))


def display_game_running_message():
    '''Display game is currently running message'''

    print('The game has not finished yet.')


def display_set_info(set_indicator: int, a_score: int, b_score, is_running: bool=True):
    '''Disply info of set'''

    print('Set %d: A (%d) | B (%d)' % (set_indicator, a_score, b_score))

    if is_running:
        display_game_running_message()


def check_deal_mode(a_score: int, b_score: int, score: int):
    '''Check that sequence is going to enter deal mode'''

    return a_score == score and b_score == score


def check_score(a_score: int, b_score: int, score: str):
    '''Check who is winner in that sequence'''

    if score == 'A':
        a_score += 1
    elif score == 'B':
        b_score += 1

    return a_score, b_score


def check_deal_win(a_score: int, b_score: int):
    '''Check that deal mode gets winner'''

    return abs(a_score - b_score) == 2


def main():
    '''Main Function'''

    sequence = input()

    a_set = 0
    b_set = 0

    set_indicator = 1

    a_score = 0
    b_score = 0

    deal_mode = False

    def set_default_score():
        '''Set score to default'''

        nonlocal a_score, b_score

        a_score = 0
        b_score = 0

    def check_set_winner(win_score: int, a_set: int, b_set: int):
        '''Check who is the winner or that set and assign set score to them'''

        nonlocal a_score, b_score
        nonlocal set_indicator

        if a_score == win_score and b_score < win_score:
            a_set += 1

            display_set_info(set_indicator, win_score,
                             b_score, is_running=False)

            set_indicator += 1
            set_default_score()
        elif b_score == win_score and a_score < win_score:
            b_set += 1

            display_set_info(set_indicator, a_score,
                             win_score, is_running=False)

            set_indicator += 1
            set_default_score()

        return a_set, b_set

    def check_deal_set_winner(a_set: int, b_set: int):
        '''Check who is winner of that set in deal mode and assign set score to them'''

        nonlocal a_score, b_score

        if a_score > b_score:
            a_set += 1
            set_default_score()
        else:
            b_set += 1
            set_default_score()

        return a_set, b_set

    for score in sequence:
        if not set_indicator:
            break

        a_score, b_score = check_score(a_score, b_score, score)

        # If this score is in last set
        if set_indicator is LAST_SET:
            if deal_mode:
                if check_deal_win(a_score, b_score):
                    display_set_info(set_indicator, a_score,
                                     b_score, is_running=False)

                    a_set, b_set = check_deal_set_winner(a_set, b_set)

                    deal_mode = False
                    set_indicator = 0

                    break

                continue

            a_set, b_set = check_set_winner(LAST_SET_WIN_SCORE, a_set, b_set)

            deal_mode = check_deal_mode(a_score, b_score, LAST_SET_DEAL_SCORE)

            continue

        if deal_mode:
            if check_deal_win(a_score, b_score):
                display_set_info(set_indicator, a_score,
                                 b_score, is_running=False)

                set_indicator += 1

                a_set, b_set = check_deal_set_winner(a_set, b_set)

                deal_mode = False

            continue

        a_set, b_set = check_set_winner(WIN_SCORE, a_set, b_set)

        deal_mode = check_deal_mode(a_score, b_score, DEAL_SCORE)

    # If A win the game
    if a_set == WIN_SET:
        display_win_message('A', b_set)
        return
    # If B win the game
    elif b_set == WIN_SET:
        display_win_message('B', a_set)
        return

    # If game is currently running in any set
    if a_score != 0 or b_score != 0:
        display_set_info(set_indicator, a_score, b_score)
        return

    # If game is currently running a new set
    if set_indicator != 0 and a_score == 0 and b_score == 0:
        display_set_info(set_indicator, 0, 0)
        return


main()
