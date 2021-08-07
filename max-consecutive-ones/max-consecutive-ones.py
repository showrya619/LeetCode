class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = [str(x) for x in nums]
        n = ''.join(n).split('0')
        return  len(max(n))
