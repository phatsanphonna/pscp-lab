'''
Week 11 - AlmostMean
https://ejudge.it.kmitl.ac.th/problem/8286
'''


def main():
    '''Main Function'''

    total_students = int(input())

    student_list = []
    avg_score = 0.0
    avg_score_list = []

    for _ in range(total_students):
        student_id, student_score = input().split('\t')

        student_list.append({student_id: float(student_score)})
        avg_score += float(student_score)

        avg_score_list.append(float(student_score))

    avg_score /= total_students

    almost_mean_student_id = ''
    almost_mean_student_score = 0.0
    almost_mean_diff_score = 9999

    for student in student_list:
        for key in student:

            diff_score = student[key] - avg_score

            if diff_score < 0 \
                    and abs(diff_score) < float(almost_mean_diff_score):
                almost_mean_student_score = str(student[key])
                almost_mean_student_id = key
                almost_mean_diff_score = abs(diff_score)

    print('%s\t%s' % (almost_mean_student_id, almost_mean_student_score))


main()
