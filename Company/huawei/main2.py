import sys

s = []
mp1=['Q','W','E','R','T','Y','U','I','O','P','A','S',
'D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
mp2=['A','B','C','D','E','F','G','H','I','J','K','L',
'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def func(s):
    for i in range(len(s)):
        if (s[i] >= 'A') & (s[i] <= 'Z'):
            for j in range(26):
                if s[i] == mp2[j]:
                    break
            print(mp1[j], end='')
        elif (s[i] >= 'a') & (s[i] <= 'z'):
            s = s[:i] + (chr)(ord(s[i]) - ord('a') + ord('A')) + s[i + 1:]
            for j in range(26):
                if (s[i] == mp2[j]):
                    break
            print((chr)(ord(mp1[j]) - ord('A') + ord('a')), end='');

        else:
            print(s[i], end=''),

if __name__ == "__main__":
    s = str(sys.stdin.readline())
    sum = func(s)

    # H kz k xif.

