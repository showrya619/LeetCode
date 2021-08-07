class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = [str(x) for x in nums]
        n = [len(x) for x in n]
        only_odd = len([num for num in n if num % 2 == 0])
        return only_odd