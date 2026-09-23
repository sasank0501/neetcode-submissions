class Solution:
    def topKFrequent(self, nums, k):
        count ={}
        for num in nums:
            if num in count:
                count[num] = count[num]+1
            else:
                count[num] = 1
        ordered = sorted (count, key = count.get, reverse = True)
        return ordered [:k]
        