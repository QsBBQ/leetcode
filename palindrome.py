# https://leetcode.com
# Valid Sudoku
# reverse integer

# Title
# 9. Palindrome Number
# example
# http://www.sanfoundry.com/c-program-reverse-number-palindrome/
# https://leetcode.com/discuss/33500/an-easy-lines-code-only-reversing-till-half-and-then-compare
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         x = str(x)
#         if x == x[::-1]:
#             return True
#         else:
#             return False
#
#
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         x = str(x)
#         len_x = len(x)-1
#         import ipdb; ipdb.set_trace()
#         # variable name to see its current value
#         # n to  move to next line
#         # c to continue
#         # l to see where we are
#         # for pasting into ipython  %paste
#         for index, item in enumerate(x):
#             #'1221'
#             if index == len_x/2:
#                 break
#             elif item == x[len_x-index]:
#                 continue
#             else:
#                 return False
#         return True
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         # note python 3 turns a int into a float with /=
#         x=int(x)
#         temp = x
#         reverse=0
#         # import ipdb; ipdb.set_trace()
#         while x > 0:
#             remainder = x%10
#             reverse = reverse*10 + remainder
#             x = int(x/10)
#         print(temp, reverse)
#         if temp == reverse:
#             return True
#         else:
#             return False


Solution().isPalindrome(10)
