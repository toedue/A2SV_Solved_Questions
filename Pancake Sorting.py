class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        size = len(arr)
        result = []


        while size > 1:
            max_value = max(arr[:size])
            indx = arr.index(max_value, 0, size)

            if indx != size - 1:
                if indx != 0:
                    ptr1, ptr2 = 0, indx
                    while ptr1 < ptr2:
                        arr[ptr1], arr[ptr2] = arr[ptr2], arr[ptr1]
                        ptr1 += 1
                        ptr2 -= 1
                    result.append(indx + 1)
                
                # flip it to its correct position (size - 1)
                i , j = 0, size-1
                while i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
                
                result.append(size)
            size -=1
            

        return result
