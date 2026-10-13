class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        totalUnits = 0
        for boxes, unitsPerBox in boxTypes:
            take = min(boxes, truckSize)
            totalUnits += take * unitsPerBox
            truckSize -= take
            if truckSize == 0:
                break
        return totalUnits