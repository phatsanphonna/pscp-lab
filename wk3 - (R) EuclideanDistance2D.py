'''
[Recommend]
Week 3 - EuclideanDistance2D
'''


def find_combine_value(x1_val, y1_val):
    '''Find combine value'''

    return (x1_val - y1_val)**2


def main():
    '''Main Function'''

    q1_val = float(input())
    q2_val = float(input())

    p1_val = float(input())
    p2_val = float(input())

    q1_p1_combine_val = find_combine_value(q1_val, p1_val)
    q2_p2_combine_val = find_combine_value(q2_val, p2_val)

    answer = (q1_p1_combine_val + q2_p2_combine_val)**0.5

    print(answer)


main()
