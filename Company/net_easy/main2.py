#coding=utf-8
import sys


def func(D, P, A):
    # 找到满足工作能力A的最大的报酬 P
    #print(A)
    paid = 0
    for i in range(len(D)):
        if (D[i] <= A) & (P[i] > paid):
            paid = P[i]
    return paid

if __name__ == "__main__":
    inputStr = sys.stdin.readline().strip()
    values1 = []
    values1.append(list(map(int, inputStr.split())))
    # print(values1)
    N = int(values1[0][0])
    M = int(values1[0][1])
    # print(N)
    # print(M)
    DiList = []
    PiList = []
    # AiList = []
    for i in range(N):
        temp = []
        jobStr = sys.stdin.readline().strip()
        temp.append(list(map(int, jobStr.split())))
        Di, Pi = int(temp[0][0]), int(temp[0][1])
        # print(Di)
        # print(Pi)
        DiList.append(Di)
        PiList.append(Pi)

    AiStr = sys.stdin.readline().strip()
    AiList = []
    #print(DiList)
    #print(PiList)
    AiList.append(list(map(int, AiStr.split())))
    for i in range(M):
        # AiList.append(int(AiStr[i]))
        paid = func(DiList, PiList, AiList[0][i])
        print(paid)


