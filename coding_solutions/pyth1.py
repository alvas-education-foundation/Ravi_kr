even_nums=[]
odd_nums=[]

a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
num_list = list(range(a,b))
for x in num_list:    
    if x % 2 == 0:        
        even_nums.append(x)
    else:       
        odd_nums.append(x)
 
print(even_nums)

print(odd_nums)

