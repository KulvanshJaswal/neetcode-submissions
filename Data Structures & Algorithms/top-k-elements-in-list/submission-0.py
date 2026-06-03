class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        return_list = []
        for num in nums:
            if num not in numbers:
                numbers[num] = 1
            else:
                numbers[num] += 1
        i = 0
        while i < k:
            return_list.append(max(numbers, key=numbers.get))
            numbers[return_list[i]] = 0
            i+=1
        return return_list
        