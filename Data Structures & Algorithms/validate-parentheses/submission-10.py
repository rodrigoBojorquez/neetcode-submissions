class Solution:
    def isValid(self, s: str) -> bool:
        pending: List[str] = []
        corresponding: Dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in corresponding.keys():
                if pending and pending[-1] == corresponding[i]:
                    pending.pop()
                else:
                    return False
            else:
                pending.append(i)
        return True if not pending else False      
                
