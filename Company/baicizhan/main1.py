#coding=utf-8
import sys

class Solution(object):
    def str2Num(self, str):
        length = len(str);
        returnNum = 0;
        for i in range(length):
            returnNum = returnNum * 10
            returnNum += int(str[i])
        return returnNum

    def MaxNum(self, s):
        if not s:
            return 0
        i = 0
        m = 0
        while i < len(s):
            strTemp = ""
            if s[i].isdigit():
                while s[i].isdigit():
                    strTemp += s[i]
                    i += 1
                    if i >= len(s):
                        break
                m = max(m, Solution().str2Num(strTemp))
            else:
                i += 1

        return m

if __name__ == "__main__":
    iputStr = str(sys.stdin.readline().strip())
    x = Solution().MaxNum(iputStr)
    print(x)

