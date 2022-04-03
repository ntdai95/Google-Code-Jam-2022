class Solution:
    def create(self, r, c):
        result = "..+"
        for _ in range(c - 1):
            result += "-+"
        result += "\n..|"
        for _ in range(c - 1):
            result += ".|"

        for _ in range(r - 1):
            result += "\n+"
            for _ in range(c):
                result += "-+"
            result += "\n|"
            for _ in range(c):
                result += ".|"

        result += "\n+"
        for _ in range(c):
            result += "-+"
        
        print(result)
    
    def punchedCards(self):
        t = int(input())
        for i in range(t):
            row_column = list(map(int, input().split(" ")))
            print(f"Case #{i + 1}:")
            self.create(row_column[0], row_column[1])

Solution().punchedCards()
