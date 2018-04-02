# 数字三角形(POJ1163)
'''
在上面的数字三角形中寻找一条从顶部到底边的路径，使得路径上所经过的数字之和最大。
路径上的每一步都只能往左下或 右下走。只需要求出这个最大和即可，不必给出具体路径。
三角形的行数大于1小于等于100，数字为 0 - 99

输入格式：

    5      //表示三角形的行数    接下来输入三角形

    7

    3   8

    8   1   0

    2   7   4   4

    4   5   2   6   5

    要求输出最大和
'''


# 法一：递归
# MaxSum(r, j)表示从D(r,j)到底边的各条路径中，最佳路径的数字之和。求 MaxSum(1,1)
# 但是运行超时   D(r, j)出发，下一步只能走D(r+1,j)或者D(r+1, j+1)


# 法二：用数组保存MaxSum(r, j)，不用重复计算
# 记忆递归型的动态规划程序：

import sys
import numpy as np

# 三角形的行数
n = int(sys.stdin.readline().strip())  # 默认是str类型
D = []
maxSum = []


def max_sum_func(i, j):
    if maxSum[i][j] != -1 :
        return maxSum[i][j]
    if i == n-1:
        maxSum[i][j] = D[i][j]
    else:
        x = max_sum_func(i+1, j)
        y = max_sum_func(i+1, j+1)
        maxSum[i][j] = max(x,y) + D[i][j]

    return maxSum[i][j]


if __name__ == "__main__":
    # 循环输入三角形的数字
    for i in range(n):
        value = sys.stdin.readline().strip()
        D_row = list(map(int, value.split()))
        D.append(D_row)
        maxSum.append(list(-1 for j in range(len(D_row))))

    max_sum = max_sum_func(0, 0)
    print(max_sum)







