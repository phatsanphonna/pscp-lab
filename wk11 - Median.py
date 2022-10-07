'''
Week 11 - Median
https://ejudge.it.kmitl.ac.th/problem/8287
'''


def main():
    '''Main Function'''

    data_length = int(input())
    data_list = []

    for _ in range(data_length):
        number = int(input())

        data_list.append(number)

    data_list = sorted(data_list)

    median_pos = (data_length + 1) / 2

    if median_pos - int(median_pos) == 0:
        median_pos = int(median_pos)

        print(format(data_list[median_pos-1], '.1f'))
    else:
        median_pos = int(median_pos)

        median_pos_1 = data_list[median_pos]
        median_pos_2 = data_list[median_pos-1]

        avg_median = (median_pos_1 + median_pos_2) / 2

        print(format(avg_median, '.1f'))


main()
