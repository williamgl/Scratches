class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1: return 2147483647

        ans, sign = 0, 1

        if dividend < 0:
            dividend, sign = -dividend, -sign
        if divisor < 0:
            divisor, sign = -divisor, -sign

        if dividend == divisor: return sign

        while dividend >= divisor:

            b = 0
            # << n means shift the bit to left n digits, i.e. multiple 2^n
            while divisor << b <= dividend:
                b += 1

            dividend -= divisor << b - 1
            ans += 1 << b - 1

        return -ans if sign < 0 else ans