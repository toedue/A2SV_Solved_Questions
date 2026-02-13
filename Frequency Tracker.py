class FrequencyTracker:

    def __init__(self):
        # hashmap to remmber how many times each number shows up
        self.number_count = {}
        # hashmap to remember how many numbers have the same count
        self.frequency_count = {}

        

    def add(self, number: int) -> None:
        #See how many times this number is already in the box
        old_count = self.number_count.get(number, 0)

        # Remove 1 from old frequency because we will increase the count
        if old_count > 0:
            self.frequency_count[old_count] -= 1
        
        #Increase the number count
        new_count = old_count + 1
        self.number_count[number] = new_count

        # Add 1 to the new frequency
        self.frequency_count[new_count] = self.frequency_count.get(new_count, 0) + 1

        

    def deleteOne(self, number: int) -> None:
        # Stop if number is not in the hashmap or already 0
        if number not in self.number_count or self.number_count[number] == 0:
            return
        
        # Old count before removing one
        old_count = self.number_count[number]
        
        # Remove 1 from old frequency
        self.frequency_count[old_count] -= 1
        
        # Decrease number count
        new_count = old_count - 1
        self.number_count[number] = new_count
        
        # If number still exists, add 1 to new frequency
        if new_count > 0:
            self.frequency_count[new_count] = self.frequency_count.get(new_count, 0) + 1

        
    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency_count.get(frequency, 0) > 0

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
