class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        ptr1, ptr2 = 0, n-1

        while ptr1 < ptr2:
            curr = numbers[ptr1] + numbers[ptr2]
            if curr == target:
                return [ptr1+1, ptr2+1]
            elif curr < target:
                ptr1 += 1
            else:
                ptr2 -=1
        return [-1, 1]
