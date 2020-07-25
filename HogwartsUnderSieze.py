# Write your code here
T = int(input())
N = input()
Q = int(input())
result = [int(char) for char in N]  

for i in range(0, Q):
    query = list(map(int,input().split()))

    if(query[2] == 0):
        for x in range(query[0], query[1]+1):
            result[x] = 1 - result[x]
    elif(query[2] == 1):
        for x in range(query[0], query[1]):
            result[x] = 1 - result[x]
        for x in range(query[1]+1, len(result)):
            result[x] = 1 - result[x]

result = [str(char) for char in result]
print("".join(result))
