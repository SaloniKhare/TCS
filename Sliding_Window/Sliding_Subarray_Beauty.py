from typing import List

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # freq[i] = count of number -(i+1) in window
        freq = [0] * 50   # covers -1 to -50

        def add(num):
            if num < 0:
                freq[-num - 1] += 1

        def remove(num):
            if num < 0:
                freq[-num - 1] -= 1

        def beauty():
            count = 0
            # iterate from most negative (-50) up to -1
            for i in range(49, -1, -1):
                count += freq[i]
                if count >= x:
                    return -(i + 1)
            return 0

        # initialize window
        for i in range(k):
            add(nums[i])

        res = [beauty()]

        # slide window
        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])
            res.append(beauty())

        return res
