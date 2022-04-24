from collections import deque


class Solution:
    def create(self, n, deliciousness_levels):
        if len(deliciousness_levels) == 1:
            return 1

        queue = deque(deliciousness_levels)
        result = 0
        current_max = 0
        while n > 1:
            if queue[0] > queue[-1]:
                current_pancake = queue.pop()
            else:
                current_pancake = queue.popleft()
            
            if current_pancake >= current_max:
                result += 1
                current_max = current_pancake
            
            n -= 1

        current_pancake = queue.pop()
        if current_pancake >= current_max:
                result += 1

        return result

    def solution(self):
        t = int(input())
        for i in range(t):
            print(f'Case #{i + 1}: {self.create(int(input()), list(map(int, input().split(" "))))}')

Solution().solution()