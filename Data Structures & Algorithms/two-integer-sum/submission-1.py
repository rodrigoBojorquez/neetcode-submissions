class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = defaultdict(int)

        for i, n in enumerate(nums):
            diff = target - n
            if diff in idx.keys():
                return [idx[diff], i]
            
            else:
                idx[n] = i

        return []