if __name__ == '__main__':
    n,q = map(int,input().split())
    h = list(map(int,input().split()))
    for i in range(q):
        query = list(map(int,input().split()))
        x= query[1]-1
        # print("x",x)
        if query[0] == 1:
            
            h[x]=query[2]
            # print(h)
        else:
            count = 0
            x= query[1]-1
            for i in range(n):
                # print("i",i)
                if i != x:
                    # print("h[x]-h[i]",h[x]-h[i])
                    if h[x]-h[i] <= x-i:
                        count += 1
                        # print("i",i)
                        # print("x",x)
            print(count)
