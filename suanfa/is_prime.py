from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    if n > 1:
        for factor in range(2, int(sqrt(n)) + 1):
            if n % factor == 0:
                return False
        return True if n != 1 else False
    return False


if __name__ == '__main__':
    is_prime(10)