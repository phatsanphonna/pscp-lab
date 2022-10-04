'''
Week 8 - Lotto
https://ejudge.it.kmitl.ac.th/problem/8243
'''


FIRST_WIN_PRIZE = 6000000
LAST_TWO_DIGIT_PRIZE = 2000
THREE_DIGIT_PRIZE = 4000
SIDE_NUMBER_WIN_PRIZE = 100000


def main():
    '''Main Function'''

    first_win = input()

    last_2_digit_win = input()

    first_3_digit_win_1 = input()
    first_3_digit_win_2 = input()

    last_3_digit_win_1 = input()
    last_3_digit_win_2 = input()

    bought_lotto = input()

    if first_win == '000000':
        first_win = '1' + first_win
    else:
        first_win = '0' + first_win

    first_win_side_1 = ('%07d' % (int(first_win) - 1))[-6:]
    first_win_side_2 = ('%07d' % (int(first_win) + 1))[-6:]

    first_win = first_win[-6:]

    def calculate_first_win(lotto: str):
        '''Calculate first win'''

        nonlocal first_win

        if first_win == lotto:
            return FIRST_WIN_PRIZE
        else:
            return 0

    def calculate_side_number_win(lotto: str):
        '''Calculate side number win'''

        nonlocal first_win_side_1, first_win_side_2

        prize = 0

        if lotto == first_win_side_1:
            prize += SIDE_NUMBER_WIN_PRIZE

        if lotto == first_win_side_2:
            prize += SIDE_NUMBER_WIN_PRIZE

        return prize

    def calculate_last_2_digit_win(lotto: str):
        '''Calculate last 2 digit win'''

        nonlocal last_2_digit_win

        if lotto[-2:] == last_2_digit_win:
            return LAST_TWO_DIGIT_PRIZE
        else:
            return 0

    def calculate_last_3_digit_win(lotto: str):
        '''Calculate last 3 digit win'''

        nonlocal last_3_digit_win_1, last_3_digit_win_2

        prize = 0

        if lotto[-3:] == last_3_digit_win_1:
            prize += THREE_DIGIT_PRIZE

        if lotto[-3:] == last_3_digit_win_2:
            prize += THREE_DIGIT_PRIZE

        return prize

    def calculate_first_3_digit_win(lotto: str):
        '''Calculate first 3 digit win'''

        nonlocal first_3_digit_win_1, first_3_digit_win_2

        prize = 0

        if lotto[:3] == first_3_digit_win_1:
            prize += THREE_DIGIT_PRIZE

        if lotto[:3] == first_3_digit_win_2:
            prize += THREE_DIGIT_PRIZE

        return prize

    total_prize = calculate_first_win(bought_lotto)
    total_prize += calculate_side_number_win(bought_lotto)
    total_prize += calculate_last_2_digit_win(bought_lotto)
    total_prize += calculate_last_3_digit_win(bought_lotto)
    total_prize += calculate_first_3_digit_win(bought_lotto)

    print(total_prize)


main()
