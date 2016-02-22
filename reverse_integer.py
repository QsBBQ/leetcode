import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Had to hard code the max 32 bit int.
        # Tried sys.maxint but it didn't work.
        x = str(x)
        if int(x)>= 2147483647 or int(x)<-2147483647:
            return 0
        elif x[0] == "-":
            negative = "-"
            x = x[1:][::-1]
            x = int(negative+x)
            if x<-2147483647:
                return 0
            else:
                return x
        else:
            x = int(x[::-1])
            if x>= 2147483647:
                return 0
            else:
                return x

# Found this on the forum. Thought it was interesting
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        return s*r * (r < 2**31)        

Solution().reverse(1234562036854775808)
