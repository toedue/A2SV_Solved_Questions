class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for string in paths:
            parts = string.split()
            folder = parts[0] 

            for i in range(1, len(parts)):
                file_name, content = parts[i].split("(")
                content = content[:-1]
                
                full_path = folder + "/" + file_name

                if content not in d:
                    d[content] = []
                d[content].append(full_path)

        # return d

        return [v for k,v in d.items() if len(v) > 1]



        
