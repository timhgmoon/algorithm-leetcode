# 3. Longest Substring Without Repeating Characters

# Time Complexity: O(n^2) ? Space Complexity: O(n)
def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    longest = 0
    curr_s = ""
    for i in range(len(s)):
        curr_length = len(curr_s)

        while s[i] in curr_s:
            curr_length -= 1
            curr_s = curr_s[1:]

        if curr_s == "":
            curr_length += 1
            curr_s += s[i]
        if s[i] not in curr_s:
            curr_length += 1
            curr_s += s[i]

        longest = max(curr_length, longest)

    return longest

# optimized solution, found is discussing by user zany_z


def lengthOfLongestSubstring2(s):
    left = 0
    chars = {}
    output = 0

    for right, char in enumerate(s):
        if char in chars:
            left = max(left, chars[char] + 1)
        output = max(output, right - left + 1)
        chars[char] = right
    return output


# s = "abcabcbb"
# s = "bbbbb"
s = "pwwkew"
print(lengthOfLongestSubstring2(s))
