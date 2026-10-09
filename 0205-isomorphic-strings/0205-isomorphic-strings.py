class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen={}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            a=s[i]
            b=t[i]
            if a in seen and seen[a] != b:
                return False
            if a not in seen and b in seen.values():
                return False
            seen[a]=b
        return True