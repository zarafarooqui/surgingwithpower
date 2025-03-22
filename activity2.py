def is_power_of_4(n):
    return n>0 and (n &(n-1))==0 and (n-1)%3==0

num=int(input("Enter a number:"))
if is_power_of_4(num):
    print(f"{num} is a power of 4.")
else:
    print(f"{num} is not a power of 4.")