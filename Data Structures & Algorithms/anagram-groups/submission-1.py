class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # buscar si hay registro en el hashmap de ese anagrama
        # si esta -> agregar string a ese listado
        # si no -> crear un nuevo listado en el hashmap
        # aplanar todos los values del hashmap en una lista de listas

        mapping: Dict[tuple, List[str]] = {}

        for s in strs:
            # comparar usando un array de frecuencia de caracteres
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            key = tuple(counts)

            if key in mapping:
                mapping[key].append(s)
            else:
                mapping[key] = [s]
        
        return list(mapping.values())