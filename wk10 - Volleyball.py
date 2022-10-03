'''
Midterm 6 - Volleyball
Week 10 - Volleyball
'''


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


def set_default_score():
    '''Set score to default'''

    return 0, 0


def main():
    '''Main Function'''

    sequence = input()

    a_set = 0
    b_set = 0

    set_indicator = 1

    a_score = 0
    b_score = 0

    deal_mode = False

    for score in sequence:
        a_score, b_score = check_score(a_score, b_score, score)

        if set_indicator == 5:
            if check_deal_mode(a_score, b_score, 14):
                deal_mode == True
                continue

            if deal_mode:
                if check_deal_win(a_score, b_score):
                    print('Set %d: A (%d) | B (%d)' %
                          (set_indicator, a_score, b_score))

                    if a_score > b_score:
                        a_set += 1
                        a_score, b_score = set_default_score()
                    else:
                        b_set += 1
                        a_score, b_score = set_default_score()

                    deal_mode = False
                    break
                continue

            if a_score == 15 and b_score < 15:
                a_set += 1
                print('Set %d: A (15) | B (%d)' % (set_indicator, b_score))
                a_score, b_score = set_default_score()
            elif b_score == 15 and a_score < 15:
                b_set += 1
                print('Set %d: A (%d) | B (15)' % (set_indicator, a_score))
                a_score, b_score = set_default_score()

            continue

        if deal_mode:
            if check_deal_win(a_score, b_score):
                print('Set %d: A (%d) | B (%d)' %
                      (set_indicator, a_score, b_score))

                set_indicator += 1

                if a_score > b_score:
                    a_set += 1
                    a_score, b_score = set_default_score()
                else:
                    b_set += 1
                    a_score, b_score = set_default_score()
        
        deal_mode = check_deal_mode(a_score, b_score, 24)

        if a_score == 25 and b_score < 25:
            a_set += 1
            print('Set %d: A (25) | B (%d)' % (set_indicator, b_score))

            set_indicator += 1
            a_score, b_score = set_default_score()
        elif b_score == 25 and a_score < 25:
            b_set += 1
            print('Set %d: A (%d) | B (25)' % (set_indicator, a_score))

            set_indicator += 1
            a_score, b_score = set_default_score()
        

    if a_score != 0 or b_score != 0:
        print('Set %d: A (%d) | B (%d)' % (set_indicator, a_score, b_score))
        print('The gane has not finished yet.')
        return

    if a_set == 3:
        print('A won 3:%d set' % b_set)
    elif b_set == 3:
        print('A won 3:%d set' % a_set)

    if a_score == 0 and b_score == 0:
        print('Set %d: A (0) | D (0)' % set_indicator)
        print('The gane has not finished yet.')
        return


main()
