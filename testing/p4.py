m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
print("Even number between m & n: ")
for i in range(min(m+1,n+1),max(m,n)):
    if i%2 == 0:
        print(i)