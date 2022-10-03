'''
Midterm 1 - Heron of Alexandria
Week 10 - Heron of Alexandria
https://ejudge.it.kmitl.ac.th/problem/8269
'''


def main():
    '''Main Function'''

    a_value = float(input())
    b_value = float(input())
    c_value = float(input())

    s_value = (a_value + b_value + c_value) / 2

    area = s_value * (s_value - a_value) * \
        (s_value - b_value) * (s_value - c_value)
    area = area**0.5

    print(format(area, '.3f'))


main()
