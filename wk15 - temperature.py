'''Week 15 - temperature'''


def main():
    '''Main Function'''

    temperature = float(input())
    temp_unit = input().upper()
    convert_unit = input().upper()

    celcius_temp = temperature

    if temp_unit != 'C':
        if temp_unit == 'F':
            celcius_temp = (temperature - 32) * 5/9
        elif temp_unit == 'K':
            celcius_temp = temperature - 273.15
        elif temp_unit == 'R':
            celcius_temp = (temperature - 491.67) * 5/9

    result_temp_celcius = celcius_temp

    if convert_unit == 'F':
        result_temp_celcius = celcius_temp * (9 / 5) + 32
    elif convert_unit == 'K':
        result_temp_celcius = celcius_temp + 273.15
    elif convert_unit == 'R':
        result_temp_celcius = celcius_temp * (9 / 5) + 491.67

    print('%.2f' % result_temp_celcius)


main()
