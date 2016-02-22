class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n%2 == 0:
            while True:
                divided = n/2
                if n == 2:
                    return True
                elif divided%2 == 1:
                    return False
                elif divided%2 == 0:
                    n = divided
                else:
                    n = divided

            return True
        else:
            return False
        # Recursive example
        # if n == 0:
        #     return False
        # elif n == 1:
        #     return True
        # elif n ==2:
        #     return True
        # elif n%2 == 1:
        #     return False
        # elif n%2 == 0:
        #     divided = n/2
        #     return self.isPowerOfTwo(divided)
