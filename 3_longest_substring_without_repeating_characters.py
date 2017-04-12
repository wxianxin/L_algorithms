# Author: Steven Wang    Date: 20170409
# 3 longest substring without repeating characters

s = "dvdf"
b = "au"
c = "abcabcbb"
d = "abcdefffffff"
e = "pwwkew"
f = "abcb"
g = "asjrgapa"

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    if len(s) == 0:
        return 0

    start = 0
    stop = 1
    result = 1

    while start != len(s) and stop < len(s):
        for _ in range(start, stop):
            if _ - start + 1 > result:
                result = _ - start + 1
                # print("_-start =", result)

            if s[_] == s[stop]:
                if stop - _ > result:
                    result = stop - _
                    # print("stop-_ =", result)
                if stop - start > result:
                    result = stop - start
                    # print("start-stop =", result, start, stop)
                start = _ + 1
                break


        if stop == len(s) - 1:
            if len(s) - start > result:
                result = len(s) - start
            break

        stop = stop + 1

    return result

print(lengthOfLongestSubstring(s))
print(lengthOfLongestSubstring(b))
print(lengthOfLongestSubstring(c))
print(lengthOfLongestSubstring(d))
print(lengthOfLongestSubstring(e))
print(lengthOfLongestSubstring(f))
print(lengthOfLongestSubstring(g))