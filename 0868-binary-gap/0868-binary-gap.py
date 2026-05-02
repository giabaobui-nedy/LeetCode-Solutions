class Solution:
    def binaryGap(self, n: int) -> int:
        binary_num = format(n, 'b')
        longest_gap = 0
        count = 0
        for char in binary_num:
            if char == '1':
                if count > 0:
                    # print("end counting...")
                    if count > longest_gap:
                        longest_gap = count
                    count = 0
                    # print("start counting...")
            count = count + 1
        return longest_gap
        