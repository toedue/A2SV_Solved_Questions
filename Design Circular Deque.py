class MyCircularDeque:

    def __init__(self, k: int):
        self.array = [0]*k
        self.k = k
        self.size = 0

        self.front = 0
        self.rear = 0

        
    def insertFront(self, value: int) -> bool:
        # cant insert if it full 
        if self.isFull():
            return False

        # move front pointer backwards(circularly)
        self.front = (self.front - 1 + self.k) % self.k
        self.array[self.front] = value

        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        # cant insert if full
        if self.isFull():
            return False

        self.array[self.rear] = value
        
        # place value at rear 
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        # just move front pointer forwards (circularly)
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        # just move rear pointer backwards (circularly)
        self.rear = (self.rear - 1 + self.k) % self.k
        self.size -=1 
        return True
        
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.array[self.front]
        
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

         # rear points to NEXT empty slot (so actual rear is one step behind)
        return self.array[(self.rear - 1 + self.k) % self.k]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
