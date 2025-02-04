class Solution:
    def romanToInt(self, s: str) -> int:
        symbol =["I","V","X","L","C","D","M"]
        value = [1,5,10,50,100,500,1000]
        json = [
            {"I": 1},
            {"V": 5},
            {"X": 10},
            {"L": 50},
            {"C": 100},
            {"D": 500},
            {"M": 1000}
        ]
        for i in range(0, len(symbol)):
            print(i)
        