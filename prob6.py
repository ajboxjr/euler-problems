end_pos = int(input("What number would you like to end on?"))

sum_of_sq = sum([ i*i for i in range(1,end_pos+1)])
sq_of_sum = sum(range(1,end_pos+1))**2

print(abs(sq_of_sum-sum_of_sq))
