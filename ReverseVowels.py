"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
class Solution:
    def is_vowel(self, c):
        return c in "aeiouAEIOU"
    
    def reverse_vowels(self, s):
        s = list(s)
        start, end = 0, len(s) - 1
        while start > end:
            if not is_vowel(self, s[start]):
                start += 1
            elif not is_vowel(self, s[end]):
                end -=1
            else:
                s[start], s[end] = s[end], s[start]
                start, end = start + 1, end - 1
        return ''.join(s)