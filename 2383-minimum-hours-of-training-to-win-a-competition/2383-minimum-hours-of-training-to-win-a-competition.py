class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res=0
        val=sum(energy)+1-initialEnergy
        if val>0:
            res+=val
        for i in experience:
            if i>=initialExperience:
                val=i-(initialExperience-1)
                res+=val
                initialExperience+=val
            initialExperience+=i
        return res