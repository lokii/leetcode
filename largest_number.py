
def strcmp(str1, str2):
    s = min(len(str1), len(str2))
    for i in range(s):
        if str1[i] != str2[i]:
            return -1 if str1[i] < str2[i] else 1
    if len(str1) > len(str2):
        return strcmp(str1[i+1 :], str2)
    if len(str1) < len(str2):
        return strcmp(str1, str2[i + 1 :])
    return 0

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
