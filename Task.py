N = list(map(int, raw_input().split()))

def reduceSUM(x, y):
    return x+y

def sortCheck(x = []):
    for i, j in enumerate(x):
        if (len(x)-1 > i):
            if (j > x[i + 1]):
                return False
    return True

def task():
    for index, j in enumerate(N):
        Right  = reduce(reduceSUM, N) - j if (index == 0) else sum(N[index+1:])

        Left = sum(N) - j if (index == len(N) - 1) else sum(N[0:index])

        print ("Left = ", Left , "Right = ", Right)

def blance():
    w = (len(N) / 2)
    for index, j in enumerate(N):
        if index < w:
            print ("head = ", index, "tail = ", len(N) - index - 1)
            if (N[index] > N[len(N) - index - 1]):
                N[index], N[len(N) - index - 1] = N[len(N) - index - 1], N[index]
                if (sortCheck(N)):
                    return True
                else:
                    N[index], N[len(N) - index - 1] = N[len(N) - index - 1], N[index]
    print ("N = ", N)
    return sortCheck(N)

if __name__ == "__main__":
    #task()
    print ("ix = ",blance())