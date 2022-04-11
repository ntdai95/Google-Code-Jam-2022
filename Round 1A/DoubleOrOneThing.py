class Solution:
    def create(self, s):
        result = [""]
        for letter in s:
            words = []
            for word in result:
                word1 = word + letter
                words.append(word1)
                word2 = word + 2*letter
                words.append(word2)

            result = words

        result.sort()
        return result[0]
    
    def solution(self):
        t = int(input())
        for i in range(t):
            print(f"Case #{i + 1}: " + self.create(input()))

Solution().solution()