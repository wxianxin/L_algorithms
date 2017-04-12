# Author: Steven Wang    Date: 20170410
# 5 longest palindromic substring
# This code works, but it is rubbish; Don't even look at it.

a = "babad"
b = "cbbd"
c = "abcdedcba"
d = "bb"
e = "ccd"
f = "aaaa"
g = "caba"


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 2 and s[0] == s[1]:
        return s

    length = 1
    middle = int((len(s)-1)/2)
    result = s[middle]
    deviation = 0

    while deviation <= middle:

        left = middle - deviation
        right = middle + deviation
        i = 1
        left_sentinel_1 = right_sentinel_1 = left_sentinel_2 = right_sentinel_2 = True

        while i <= len(s) - right - 1:
            # abcba
            if left - i >= 0 and left_sentinel_1 and s[left - i] == s[left + i]:
                if 2*i + 1 > length:
                    length = 2*i + 1
                    result = s[left - i : left + i + 1]
            else:
                left_sentinel_1 = False

            if right - i >= 0 and right_sentinel_1 and s[right - i] == s[right + i]:
                if 2*i + 1 > length:
                    length = 2*i + 1
                    result = s[right - i : right + i + 1]
            else:
                right_sentinel_1 = False

            i = i + 1

            # abba
        i = 1
        while i <= len(s) - right:
            if left - i >= 0 and left_sentinel_2 and s[left - i] == s[left + i - 1]:
                if 2 * i > length:
                    length = 2*i
                    result = s[left - i: left + i]
            else:
                left_sentinel_2 = False

            if right - i >= 0 and right_sentinel_2 and s[right - i] == s[right + i - 1]:
                if 2 * i > length:
                    length = 2*i
                    result = s[right - i: right + i]
            else:
                right_sentinel_2 = False

            i = i + 1

        deviation = deviation + 1

    return result

print(longestPalindrome(a))
print(longestPalindrome(b))
print(longestPalindrome(c))
print(longestPalindrome(d))
print(longestPalindrome(e))
print(longestPalindrome(f))
print(longestPalindrome(g))