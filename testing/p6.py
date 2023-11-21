n=int(input("The No. of stars: "))
for i in range(1,n+1):
    print(' '*n, end='')
    print('* '*(i))
    n-=1