N=input("Enter a number N:")
odd_sum=0
even_sum=0
even_counter=0
for i in range(1, int(N)+1):
    if(i%2==0):
        even_sum+=i
        even_counter+=1
    else:
        odd_sum+=i
print("Sum of the odd numbers:", odd_sum)
print("Average of the even numbers:", even_sum/even_counter)