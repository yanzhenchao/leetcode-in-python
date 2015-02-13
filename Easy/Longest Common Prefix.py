#1 Compare letter by letter

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        pre = ''
        if strs != []:
            minStrLength = len(strs[0])
            for s in strs:
                if len(s) < minStrLength:
                    minStrLength = len(s)
            for i in range(minStrLength):
                for j in range(1, len(strs)):
                    if strs[j][i] != strs[0][i]:
                        return pre
                pre += strs[0][i]
        return pre
