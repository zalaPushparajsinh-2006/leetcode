class Solution {
public:
    int smallestEvenMultiple(int n) {
        // Intuition: if n already even, it's the answer; else double it to make it even
        if (n % 2 == 0) return n;
        return n * 2;
    }
};