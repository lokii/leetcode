class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s.strip()
        words = s.split(' ')
        words = [w for w in words if len(w) > 0]
        words.reverse()
        return ' '.join(words)

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords(" the sky is      blue "))
    print(solution.reverseWords("   a   b "))
