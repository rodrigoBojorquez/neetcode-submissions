class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store the value and index
        counter: Dict[int, int] = {}
        result = []

        for i, value in enumerate(nums):
            diff = target - value
            if counter.get(diff) != None:
                result.append(counter.get(diff, 0))
                result.append(i)
            else:
                counter[value] = i
        
        return result