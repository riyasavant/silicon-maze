n,k,s = map(int,input().split())

count = 0
maximum = 0

for x in str(s):
    if x == '1':
        count += 1
    else:
        if(count > maximum):
            maximum = count
        count = 0

if(maximum+k <= n):
    print(maximum+k)
    
else:
    print(maximum)




