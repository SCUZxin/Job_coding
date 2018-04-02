#coding=utf-8
import sys
import math

if __name__ == "__main__":
    value = []
    for i in range(21):
        v = int(sys.stdin.readline().strip())
        value.append(v)

    sum = 0
    index = 0
    for i in range(21-3):
        tempV = value[i]+value[i+1]+value[i+2]+value[i+3]
        if tempV > sum:
            index = i
        sum = max(sum, tempV)

    print(index)

