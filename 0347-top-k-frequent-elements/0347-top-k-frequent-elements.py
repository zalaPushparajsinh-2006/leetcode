class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in nums:
                hashmap[i]+=1
        hashmap = list(sorted(hashmap.items(), key=lambda x: x[1],reverse=True))

        output=[i[0] for i in hashmap[:k]]
        return output

        