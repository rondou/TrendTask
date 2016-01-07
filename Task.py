N = list(map(int, raw_input().split()))

def reduceSUM(x, y):
    return x+y

def task():
    q = reduce(reduceSUM, N)
    print("qq = ", q)

    for index, j in enumerate(N):
        Right  = reduce(reduceSUM, N) - j if (index == 0) else sum(N[index+1:])

        Left = sum(N) - j if (index == len(N) - 1) else sum(N[0:index])

        print ("Left = ", Left , "Right = ", Right)

if __name__ == "__main__":
    task()