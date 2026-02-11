class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False
        current = ""
        
        for line in source:
            i = 0
            
            while i < len(line):
                
                # start block comment
                if not in_block and i+1 < len(line) and line[i] == "/" and line[i+1] == "*":
                    in_block = True
                    i += 2
                
                # end block comment
                elif in_block and i+1 < len(line) and line[i] == "*" and line[i+1] == "/":
                    in_block = False
                    i += 2
                
                # single line comment
                elif not in_block and i+1 < len(line) and line[i] == "/" and line[i+1] == "/":
                    break
                
                # normal character
                elif not in_block:
                    current += line[i]
                    i += 1
                
                else:
                    i += 1
            
            # add line if not inside block comment
            if not in_block and current:
                result.append(current)
                current = ""
        
        return result
