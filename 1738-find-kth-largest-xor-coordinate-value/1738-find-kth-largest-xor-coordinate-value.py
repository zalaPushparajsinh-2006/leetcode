class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0]) # dimensions 
        
        vals = []
        for i in range(m): 
            for j in range(n): 
                if i: matrix[i][j] ^= matrix[i-1][j]
                if j: matrix[i][j] ^= matrix[i][j-1]
                if i and j: matrix[i][j] ^= matrix[i-1][j-1]
                vals.append(matrix[i][j])
        
        def part(lo, hi): 
            """Partition vals from lo (inclusive) to hi (exclusive)."""
            i, j = lo+1, hi-1
            while i <= j: 
                if vals[i] < vals[lo]: i += 1
                elif vals[lo] < vals[j]: j -= 1
                else: 
                    vals[i], vals[j] = vals[j], vals[i]
                    i += 1
                    j -= 1
            vals[lo], vals[j] = vals[j], vals[lo]
            return j 
        
        lo, hi = 0, len(vals)
        while lo < hi: 
            mid = part(lo, hi)
            if mid + k < len(vals): lo = mid + 1
            else: hi = mid
        return vals[lo]