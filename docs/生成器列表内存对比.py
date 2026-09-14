# 显示当前 python 程序占用的内存大小(对比列表与生成器的内存占用情况)
import os
import psutil


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024.0 / 1024
    print("{} memory used: {} MB".format(hint, memory))


def test_iterator():
    show_memory_info("initing iterator")
    list_1 = [i for i in range(100000000)]
    show_memory_info("after iterator initiated")
    print(sum(list_1))
    show_memory_info("after sum called")


def test_generator():
    show_memory_info("initing generator")
    list_2 = (i for i in range(100000000))
    show_memory_info("after generator initiated")
    print(sum(list_2))
    show_memory_info("after sum called")


test_generator()
print("---------" * 10)
test_iterator()
show_memory_info("脚本执行结束")

"""
测试结果输出如下所示:
initing generator memory used: 30.3515625 MB
after generator initiated memory used: 30.3515625 MB
4999999950000000
after sum called memory used: 30.3515625 MB
------------------------------------------------------------------------------------------
initing iterator memory used: 30.3515625 MB
after iterator initiated memory used: 2862.09375 MB
4999999950000000
after sum called memory used: 3579.6015625 MB
脚本执行结束 memory used: 8.2578125 MB

从提供的输出结果来看，我们可以观察到几个关键点，这有助于理解 Python 中的内存管理和释放机制：
1. **生成器 (`test_generator` 函数) 的内存使用**：
   - 在生成器初始化后，内存使用几乎没有变化，这是因为生成器是惰性的，它们仅在需要时才计算下一个值，因此不会像列表那样一次性占用大量内存。
   - 在 `sum` 调用后，内存使用依然没有显著变化，这表明生成器在迭代过程中并没有导致大量内存的分配。

2. **迭代器（列表） (`test_iterator` 函数) 的内存使用**：
   - 列表初始化后，内存使用显著增加，这是因为列表是一次性将所有元素加载到内存中的数据结构，对于大量数据来说，会占用大量内存。
   - 在 `sum` 调用后，内存使用进一步增加，这可能是因为 `sum` 函数在执行过程中可能有额外的内存分配（例如，累加求和可能需要临时变量）。但是，这里内存使用量的大幅增加可能与其他因素有关，如 Python 的内存分配策略、垃圾回收机制的工作时机等。

3. **函数执行结束后的内存释放**：
   - 在最后的输出中，我们看到内存使用量回落到了 8.2578125 MB，这比列表初始化前的内存使用量稍高。这表明在函数执行结束后，大部分通过列表分配的内存已经被释放。
   - 需要注意的是，内存的释放并不意味着立即返回给操作系统。Python 的内存分配器可能会保留这部分内存以供后续的 Python 对象使用，这是为了提高内存分配的效率。

结论:
- 函数执行结束后，局部变量（如大列表）所占用的内存确实会被标记为可回收，进而被 Python 的垃圾回收机制回收。但具体的内存释放时机和是否立即返还给操作系统，取决于 Python 解释器的内存管理策略和垃圾回收机制。
- 在实际应用中，如果遇到内存敏感的场景，推荐使用更节省内存的数据结构（如生成器），并且注意及时释放不再使用的大对象，以协助垃圾回收机制更高效地回收内存。
"""
