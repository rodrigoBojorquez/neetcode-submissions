class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # define a global top score
        top_score: int = 0
        local_score: int = 0

        # loop into the array
        for i in nums:
            # increase the local store
            if i == 1:
                local_score += 1
                if local_score > top_score:
                    top_score = local_score
            # check if the local is greater than the top_score and reset local
            else:
                if local_score > top_score:
                    top_score = local_score
                local_score = 0
        return top_score