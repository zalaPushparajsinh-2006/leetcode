class Solution:
    def removeDigit(self, num_str, digit_str):
        prev_i = 0
        i = num_str.find(digit_str, prev_i)
        max_num = None
        while (i >= 0):
            curr_num_str = num_str[:i] + num_str[i+1:]
            curr_num = int(curr_num_str)
            if (max_num is None or curr_num >= max_num):
                max_num = curr_num
            prev_i = i + 1
            i = num_str.find(digit_str, prev_i)
        return str(max_num)