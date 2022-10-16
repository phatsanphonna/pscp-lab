'''
Week 11 - Diamond I
https://ejudge.it.kmitl.ac.th/problem/8293
'''


def main():
    '''Main Function'''

    row = int(input())
    column = int(input())

    matrix = []

    for _ in range(row):
        input_column = input().split(' ')
        input_column = [int(i) for i in input_column]

        matrix.append(input_column)

    most_valuable_column = float('-inf')

    for i in range(column):
        total_stuff = 0

        for j in range(row):
            total_stuff += matrix[j][i]

        if total_stuff > most_valuable_column:
            most_valuable_column = total_stuff

    print(most_valuable_column)


main()
