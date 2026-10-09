class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and rom[s[i]] < rom[s[i + 1]]:
                total -= rom[s[i]]
            else:
                total += rom[s[i]]

        return total