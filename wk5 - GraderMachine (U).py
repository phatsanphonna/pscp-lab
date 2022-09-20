'''
Week 5 - GraderMachine
- ติด Testcase รองสุดท้าย
'''


def main():
    '''Main Function'''

    start = int(input())
    stop = int(input())

    progress = ''
    _sum = 0

    for i in range(start, stop+1):
        if not i % 2 == 0:
            continue

        _sum += i
        progress += '%d ' % i

    print('pass : ' + progress.rstrip())
    print('Sum : %d' % _sum)


main()
