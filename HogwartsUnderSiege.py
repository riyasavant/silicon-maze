T = int(input())  

while(T>0):
    N = input()
    Q = int(input())
    number = ''

    def change(string):
        new = ''
        for x in range(0, len(string)):
            new += '0' if string[x] == '1' else '1'
        return new
    
    for i in range(0, Q):
        query = list(map(int,input().split()))
        a = query[0]
        b = query[1]
        if(query[2] == 0):
            number = (N[0:a] + change(N[a:b+1]) + N[b+1:]) if number == '' else (number[0:a] + change(number[a:b+1]) + number[b+1:])
  
        elif(query[2] == 1):
            number = (change(N[0:a]) + N[a:b+1] + change(N[b+1:])) if number == '' else (change(number[0:a]) + number[a:b+1] + change(number[b+1:]))
        
    print(number)       
    T = T - 1
