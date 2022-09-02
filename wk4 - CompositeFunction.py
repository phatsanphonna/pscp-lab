'''Week 4 - CompositeFunction'''
 
 
def function_f(x_value: int):
    '''f(x)'''
 
    return 2 * x_value
 
 
def function_g(x_value: int):
    '''g(x)'''
 
    return (x_value / 2) + 1
 
 
def main():
    '''Main Function'''
 
    x_value = int(input())
 
    print('%.2f' % function_f(function_g(x_value)))
    print('%.2f' % function_g(function_f(x_value)))
 
 
main()