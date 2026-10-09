class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen={}  
        w=s.split()
        if len(pattern)!=len(w):
            return False
        for i in range(len(pattern)):
            a=pattern[i]
            b=w[i]
            if a in seen and seen[a] != b:
                return False
            if a not in seen and b in seen.values():
                return False
            seen[a]=b
        return True