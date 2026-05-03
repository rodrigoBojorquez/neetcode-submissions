import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        heap = []

        for n, f in frequency.items():
            heapq.heappush(heap, (f, n))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result