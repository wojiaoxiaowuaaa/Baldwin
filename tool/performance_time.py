from time_count import calculate_execution_time
import cProfile


@calculate_execution_time
def sum_(n):
    """装饰器统计出来的执行耗时与cProfile统计出来的一致"""
    count = 0
    for i in range(n):
        count += i
    # print(count)
    return count


if __name__ == '__main__':
    cProfile.run("sum_(100000000)")
