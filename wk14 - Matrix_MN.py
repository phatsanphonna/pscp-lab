'''Week 14 - Matrix_MN'''


def main():
    '''Main Function'''

    row = int(input())
    column = int(input())

    matrix = []

    for _ in range(row):
        pre_matrix = []

        for _ in range(column):
            number = input()

            pre_matrix.append(number)

        matrix.append(pre_matrix)

    for pre_matrix in matrix:
        print(*pre_matrix, sep=' ')


main()
