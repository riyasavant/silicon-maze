if __name__ == "__main__":
    n , q = map(int,input().split())
    a = input()
    arr = [int(i) for i in a]

    for i in range(q):
        # print(arr)
        query = list(map(int,input().split()))
        # print("query[1]-1",query[1]-1)
        # print("query[2]-1", query[2] - 1)
        if query[0] == 0:
            for i in range(query[1]-1,query[2]):
                # print("i",i)
                arr[i] = 1
                # print(arr)

        else:
            count = 0
            # print("count",count)
            for i in range(query[1]-1,query[2]):
                    count = count * 2 + arr[i]
                    # print("count", count)
            print(count)
