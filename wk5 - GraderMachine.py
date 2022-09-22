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

    if start < stop:
        while start <= stop:
            if start % 2 == 0:
                _sum += start
                progress += '%d ' % start
            start += 1

    else:
        while start >= stop:
            if start % 2 == 0:
                _sum += start
                progress += '%d ' % start
            start -= 1

    print('pass : ' + progress.rstrip())
    print('Sum : %d' % _sum)


main()
