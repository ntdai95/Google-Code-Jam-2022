class Solution:
    def find_straight_number(self, n, s):
        s.sort(reverse=True)
        n = min(n, s[0])
        while n > 0:
            for i, number in enumerate(s):
                if number < n - i:
                    n -= 1
                    
                if i == n - 1:
                    return str(n)
    
    def d1000000(self):
        t = int(input())
        for i in range(t):
            print(f"Case #{i + 1}: " + self.find_straight_number(int(input()), list(map(int, input().split(" ")))))

Solution().d1000000()
