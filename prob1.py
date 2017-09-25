'''
Problem 1:
Multiples of 3 and 5
'''
print("Problem 1: Multiples of 3 and 5")

end_pos = int( input("What is the end position obtain [0... "))
sum_total = 0
for index in range(end_pos):
    if(index%3==0 or index%5==0):
        sum_total += index
        print("mult:{}, total:{}".format(index,sum_total))
print("The sum from 0 to {} is {}".format(end_pos, sum_total))
