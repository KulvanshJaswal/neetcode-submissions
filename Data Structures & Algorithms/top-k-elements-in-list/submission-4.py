class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for num in nums:
            if num not in numbers:
                numbers[num] = 1
            else:
                numbers[num] += 1
        freq_array = [[] for i in range(len(nums) + 1)]
        for key, value in numbers.items():
            freq_array[value].append(key)
        return_list =[]
        i=1
        while True:
            return_list = return_list + freq_array[0-i]
            if len(return_list) >= k:
                return return_list[0:k]
            i+=1