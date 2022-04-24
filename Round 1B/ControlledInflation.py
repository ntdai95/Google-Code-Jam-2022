class Solution:
    def create(self, np):
        n = np[0]
        products = [list(map(int, input().split(" "))) for _ in range(n)]
        if n == 1:
            return max(products[0])

        result = 0
        i = 0
        current_pump_pressure = 0
        while i < n - 1:
            current_product = products[i]
            min_current_product = min(current_product)
            max_current_product = max(current_product)
            next_product = products[i + 1]
            min_next_product = min(next_product)
            max_next_product = max(next_product)
            if current_pump_pressure <= min_current_product and current_pump_pressure <= max_current_product:
                result += max_current_product - current_pump_pressure
                current_pump_pressure = max_current_product
            elif current_pump_pressure > min_current_product and current_pump_pressure > max_current_product:
                result += current_pump_pressure - min_current_product
                current_pump_pressure = min_current_product
            elif abs(current_pump_pressure - min_current_product) + min(abs(max_current_product - min_next_product), abs(max_current_product - max_next_product)) >= abs(current_pump_pressure - max_current_product) + min(abs(min_current_product - min_next_product), abs(min_current_product - max_next_product)):
                result += abs(current_pump_pressure - max_current_product) + max_current_product - min_current_product
                current_pump_pressure = min_current_product
            else:
                result += abs(current_pump_pressure - min_current_product) + max_current_product - min_current_product
                current_pump_pressure = max_current_product

            i += 1
        
        current_product = products[-1]
        min_current_product = min(current_product)
        max_current_product = max(current_product)
        if current_pump_pressure <= min_current_product and current_pump_pressure <= max_current_product:
            result += max_current_product - current_pump_pressure
            current_pump_pressure = max_current_product
        elif current_pump_pressure > min_current_product and current_pump_pressure > max_current_product:
            result += current_pump_pressure - min_current_product
            current_pump_pressure = min_current_product
        elif abs(current_pump_pressure - min_current_product) > abs(current_pump_pressure - max_current_product):
            result += abs(current_pump_pressure - max_current_product) + max_current_product - min_current_product
            current_pump_pressure = min_current_product
        else:
            result += abs(current_pump_pressure - min_current_product) + max_current_product - min_current_product
            current_pump_pressure = max_current_product

        return result

    def solution(self):
        t = int(input())
        for i in range(t):
            print(f'Case #{i + 1}: {self.create(list(map(int, input().split(" "))))}')

Solution().solution()