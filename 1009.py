def bitwiseComplement(self, n: int) -> int:
    for i in range(1, 31):
        if 2 ** i > n:
            return 2 ** i - n - 1