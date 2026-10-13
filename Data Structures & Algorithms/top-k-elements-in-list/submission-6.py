class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        rtrn = []

        for i in range(k):
            rtrn.append(max(freq, key = freq.get))
            freq[rtrn[i]] = 0

        return rtrn


