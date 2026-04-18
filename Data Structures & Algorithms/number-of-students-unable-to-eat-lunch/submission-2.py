class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        counter = Counter(students)

        for s in sandwiches:
            # if there's students that want that sandwich
            if counter[s] > 0:
                res -= 1
                counter[s] -= 1
            # there's no students wanted that sandwich
            else:
                return res
        return res