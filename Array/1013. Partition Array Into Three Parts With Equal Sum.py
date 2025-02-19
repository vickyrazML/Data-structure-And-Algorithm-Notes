from ast import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total =sum(arr)
        if total%3 !=0:
            return False
        reqsum = total // 3
        partsum, count =0,0
        for num in arr:
            if count == 2:
                return True
            partsum += num
            if partsum == reqsum:
                partsum = 0
                count += 1
        return False
