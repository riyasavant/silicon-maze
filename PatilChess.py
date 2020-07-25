N = int(input())

for x in range(0, N):
    if(N == 2 or N == 1):
        print('1 '*N)
    else:
        if(N%2 == 0):
            print('0 '*N)
        else:
            for i in range(1, N+1):
                half = N//2
                if(i%2 == 0):
                    print('1 0 '*half, end='')
                    print('1 ')
                else:
                    print('0 1 '*half, end='')
                    print('0 ')
            break
