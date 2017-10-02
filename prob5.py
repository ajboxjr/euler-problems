try:
    max_mult = int(input("Enter a range of multiples"))
except:
    print("sorry that was not a valid input")
mult_range = {index:False for index in range(1,max_mult+1)}
for key, val in mult_range.items():
    print(key,val)

def are_all_multiples(mult_range, multiple):
    return all( multiple%int(k) ==0 for k,val in mult_range.items())

smlst_multiple = 1
while(not are_all_multiples(mult_range, smlst_multiple)):
       smlst_multiple +=1

print(smlst_multiple)
