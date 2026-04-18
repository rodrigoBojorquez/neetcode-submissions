class Solution:
    def isValid(self, s: str) -> bool:
        pending: List[str] = []
        corresponding: Dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            # if i in corresponding.values():
            #     pending.append(i)
            # elif pending and i in corresponding.keys():
            #     if pending[-1] == corresponding[i]:
            #         pending.pop()
            # else:
            #     return False

            if i in corresponding.keys():
                # no se puede iniciar con un cierre
                if not pending:
                    return False
                # quitar pendiente
                if pending[-1] == corresponding[i]:
                    pending.pop()
                else:
                    return False
            

            # agregar un pendiente
            else:
                pending.append(i)

        
        return True if not pending else False
            
                
