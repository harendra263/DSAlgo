class Solution:
    def myAtoi(self, s: str) -> int:
        if (ord(s[0]) >=48 and ord(s[0])<=57) or ord(s[0]) ==45 or ord(s[0]) == 43 or ord(s[0]) == 32:
            sign = 1
            for i in s:
                if ord(i) == 43:
                    sign *= 1
                elif ord(i) == 45:
                    sign *= -1


            s  = list(s)
            result = "".join(item for item in s if ord(item) >= 48 and ord(item) <= 57)
            result = int(result)
            if sign != "a":
                samir = int(sign * result)
                if samir >= -2**31 and samir <= 2**31-1:
                    return samir
                else:
                    return (-(2**31)) if samir < -(2**31) else (2**31-1)
            elif result >= -2**31 and result<= 2**31-1:
                return result
            else:
                return (-(2**31)) if result  < -(2**31) else 2**31-1
        return 0


s = "3hsh 2.dhhf-   jjf    4159"
ll = Solution()
print(ll.myAtoi(s))


