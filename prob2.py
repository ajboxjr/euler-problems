def fib(end_pos):
    x,y = 0,1
    even_fib_sum = 0
    for _ in range(end_pos):
        x,y = y,x+y
        if(y > 4000000):
            break
        if(is_even(y)):
            print('{} + {} = {}'.format(y,even_fib_sum, y+even_fib_sum))
            even_fib_sum +=y
            print("Even {}".format(y))
    print("sum is: {}".format(even_fib_sum))

def is_even(fib_num):
    if(fib_num%2==0):
        return True
    else:
        return False

fib(int(input("Which number would you like to go to")))
