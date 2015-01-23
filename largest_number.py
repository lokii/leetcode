def strcmp(str1, str2):
    return -1 if str1 + str2 < str2 + str1 else 1

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        if (num.count(0) == len(num)):
            return '0'
        numstr = [str(c) for c in num]
        numstr.sort(cmp = strcmp, reverse = True)
        return ''.join(numstr)

if __name__ == '__main__':
    print(strcmp("824", "8247"))
    print(strcmp("300", "30"))
    print(strcmp("121", "12"))
    solution = Solution()
    print(solution.largestNumber([9, 34, 30, 5, 3]))
    print(solution.largestNumber([0, 0]))
