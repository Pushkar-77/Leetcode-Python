class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        w=""
        for i in s:
            if i.isalpha():
                w += i
        
        new=""
        for i in s:
            if i.isalpha():
                new += w[-1]
                w = w[:-1]
            else:
                new +=i
        return new

