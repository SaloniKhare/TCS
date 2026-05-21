from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0

        for right, fruit in enumerate(fruits):
            count[fruit] += 1

            # shrink window if more than 2 distinct fruits
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            # update max length
            max_len = max(max_len, right - left + 1)

        return max_len
