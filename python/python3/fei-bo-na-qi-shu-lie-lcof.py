class Solution:
    def fib(self, n: int) -> int:

        res = [0, 1]
        if n <= 1:
            return res[n]
        for i in range(2, n + 1):
            res.append(res[i-1] + res[i-2])
            print(res)
        return res[-1]


if __name__ == '__main__':
    print(Solution().fib(45))