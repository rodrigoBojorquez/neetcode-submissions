class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: List[int] = []

        # iterate the operations
        for o in operations:
            # if o is '+'
            if o == '+':
                record.append(record[-1] + record[-2])
            elif o == 'D':
                record.append(record[-1] * 2)
            elif o == 'C':
                record.pop()
            else:
                record.append(int(o))

        return sum(record)