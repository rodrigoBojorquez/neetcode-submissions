class Solution:
    def isValid(self, s: str) -> bool:
        pending: List[str] = []
        close_to_open: Dict[str, str] = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for i in s:
            if i in close_to_open:
                if pending and pending[-1] == close_to_open[i]:            
                    pending.pop()
                else:
                    return False
            else:
                pending.append(i) 
        return True if not pending else False
