'''
Week 8 - SecondConverter
https://ejudge.it.kmitl.ac.th/problem/8248
'''


def main():
    '''Main Function'''

    total_seconds = int(input())

    assign_second = int(input())
    assign_minute = int(input())
    assign_hour = int(input())

    minutes, seconds = divmod(total_seconds, assign_second)
    hours, minutes = divmod(minutes, assign_minute)
    _, hours = divmod(hours, assign_hour)

    print('%d:%d:%d' % (hours, minutes, seconds))


main()
