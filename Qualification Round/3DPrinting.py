class Solution:
    def find_color(self, printer1, printer2, printer3):
        result = [min(printer1[i], printer2[i], printer3[i]) for i in range(4)]
        if sum(result) < 1000000:
            return "IMPOSSIBLE"
        
        total = 1000000
        for i, number in enumerate(result):
            if total > 0:
                if number > total:
                    result[i] = total
                    total = 0
                else:
                    total -= number
            else:
                result[i] = 0
        
        print_result = ""
        for number in result:
            print_result += str(number) + " "
        
        return print_result[:-1]

    
    def printing(self):
        t = int(input())
        for i in range(t):
            printer1 = list(map(int, input().split(" ")))
            printer2 = list(map(int, input().split(" ")))
            printer3 = list(map(int, input().split(" ")))
            print(f"Case #{i + 1}: " + self.find_color(printer1, printer2, printer3))

Solution().printing()
