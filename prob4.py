largest_product = 0
for multiplicand in range(100,1000):
    for multiplicator in range(100,1000):
        product = multiplicand*multiplicator
        if(str(product)[::-1] == str(product)):
            print("{}*{} = {}".format(multiplicand, multiplicator,product))
            if(product > largest_product):
                largest_product = product

print(largest_product)
        
        
