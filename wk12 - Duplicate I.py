'''
Week 12 - Duplicate I
https://ejudge.it.kmitl.ac.th/problem/8325
'''


def main():
    '''Main Function'''

    group_m_total = int(input())
    group_n_total = int(input())

    group_m = []

    for _ in range(group_m_total):
        student_id = input()

        group_m.append(student_id)

    duplicate_id = []

    for _ in range(group_n_total):
        student_id = input()

        if student_id in group_m:
            duplicate_id.append(student_id)

    if not duplicate_id:
        print('Nope')
        return

    duplicate_id = sorted(duplicate_id, reverse=True)

    print(*duplicate_id, sep='\n')


main()
