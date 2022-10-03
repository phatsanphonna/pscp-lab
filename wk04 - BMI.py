'''Week 4 - BMI'''


def calculate_bmi(weight: float, height: float):
    '''Calculate BMI'''

    return weight / (height / 100)**2


def main():
    '''Main Function'''

    person1_name = input()
    person1_weight = float(input())
    person1_height = float(input())

    person2_name = input()
    person2_weight = float(input())
    person2_height = float(input())

    person3_name = input()
    person3_weight = float(input())
    person3_height = float(input())

    person4_name = input()
    person4_weight = float(input())
    person4_height = float(input())

    person5_name = input()
    person5_weight = float(input())
    person5_height = float(input())

    print("%s's  BMI = %.2f" %
          (person1_name, calculate_bmi(person1_weight, person1_height)))
    print("%s's  BMI = %.2f" %
          (person2_name, calculate_bmi(person2_weight, person2_height)))
    print("%s's  BMI = %.2f" %
          (person3_name, calculate_bmi(person3_weight, person3_height)))
    print("%s's  BMI = %.2f" %
          (person4_name, calculate_bmi(person4_weight, person4_height)))
    print("%s's  BMI = %.2f" %
          (person5_name, calculate_bmi(person5_weight, person5_height)))


main()
