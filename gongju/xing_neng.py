import cProfile


def sum_(n):
    count = 0
    for i in range(n):
        count += i
    # print(count)
    return count


cProfile.run("sum_(100000000)")
