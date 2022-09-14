"""Grade III"""


def gradecal(grade):
    """cal grade"""
    gpa = 0

    if grade >= 95:
        gpa = 4
    elif grade >= 90:
        gpa = 3.5
    elif grade >= 85:
        gpa = 3
    elif grade >= 80:
        gpa = 2.5
    elif grade >= 75:
        gpa = 2
    elif grade >= 70:
        gpa = 1.5
    elif grade >= 65:
        gpa = 1
    elif grade >= 60:
        gpa = 0.5
    else:
        gpa = 0

    return gpa


def main():
    """Grade III"""

    num = int(input())

    grade_sum = 0
    for _ in range(num):
        scr_x = float(input())
        gpa = gradecal(scr_x)
        grade_sum += gpa

    gpa_average = int((grade_sum / num) * 100)
    gpa_average = gpa_average / 100

    print("%.2f" % gpa_average)


main()
