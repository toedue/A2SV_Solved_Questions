import random

class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.listt = []
        
    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.dic[val] = len(self.listt)
            self.listt.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.dic:
            idx = self.dic[val]
            last = self.listt[-1]

            self.listt[idx], self.listt[-1] = self.listt[-1], self.listt[idx]

            # update dictionary
            self.dic[last] = idx

            # delete val from dictionary
            del self.dic[val]
            self.listt.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.listt)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
