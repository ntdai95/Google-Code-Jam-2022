class Solution:
    def subset_sum(self, data, target, partial=[]):
        s = sum(partial)

        if s == target:
            return partial

        if s >= target:
            return
        
        for i in range(len(data)):
            n = data[i]
            remaining = data[i + 1:]
            result = self.subset_sum(remaining, target, partial + [n])
            if result:
                return result

    def create(self, n):
        result = []
        for i in range(n):
            result.append(i + 1)

        print(*result, flush=True)
        b = list(map(int, input().split()))
        result += b
        half_sum = int(sum(result) / 2)
        print(*self.subset_sum(result, half_sum), flush=True)

    def solution(self):
        t = int(input())
        for _ in range(t):
            self.create(int(input()))

Solution().solution()