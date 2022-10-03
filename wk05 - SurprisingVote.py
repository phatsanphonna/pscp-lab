'''Week 5 - SurprisingVote'''


def main():
    '''Main Function'''

    total_vote = float(input())
    highest_vote = float(input())
    average_of_2_votes = 0

    if highest_vote * 2 < total_vote:
        average_of_2_votes = total_vote - highest_vote * 2

    if highest_vote - average_of_2_votes > 2:
        print('Surprising')
    else:
        print('Not surprising')


main()
