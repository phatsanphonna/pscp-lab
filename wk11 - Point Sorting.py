'''
Week 11 - Point Sorting
https://ejudge.it.kmitl.ac.th/problem/8290
'''


def main():
    '''Main Function'''

    loops = int(input())

    for _ in range(loops):
        total_data = int(input())

        data_list = []

        for _ in range(total_data):
            data = input().split(' ')
            data = [int(num) for num in data]

            data_list.append(data)

        data_list.sort(key=lambda pos: pos[1], reverse=True)
        data_list.sort(key=sum)

        for pos in data_list:
            print(*pos, sep=' ')


main()
