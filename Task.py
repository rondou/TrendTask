N = list(map(int, input().split()))

for index, j in enumerate(N):

    Right  = sum(N) - j if (index == 0) else sum(N[index+1:])

    Left = sum(N) - j if (index == len(N) - 1) else sum(N[0:index])

    print ("Left = ", Left , "Right = ", Right)
