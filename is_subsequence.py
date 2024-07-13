"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

class Solution:
    def isSubsequence(self, s, t):
        len_s, len_t = len(s), len(t)
        p_s, p_t = 0, 0
        while p_s < len_s and p_t < len_t:
            if s[p_s] == t[p_t]:
                p_s += 1
            p_t += 1
        return p_s == len_s
                
