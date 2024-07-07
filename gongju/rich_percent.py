# import time
# from rich.progress import track
#
# class TimeConsumingTask:
#     def __init__(self, total_iterations):
#         self.total_iterations = total_iterations
#
#     def execute(self):
#         """
#         执行耗时操作，并在执行过程中显示进度条。
#         """
#         for i in track(range(self.total_iterations), description="Processing run"):
#             # 模拟耗时操作
#             time.sleep(0.1)  # 暂停0.1秒
#             # 在这里可以添加你的业务逻辑
#
# # 使用示例
# if __name__ == "__main__":
#     task = TimeConsumingTask(total_iterations=10)
#     task.execute()

import time
from rich.progress import Progress

class TimeConsumingTask:
    def __init__(self, total_iterations):
        self.total_iterations = total_iterations

    def execute(self):
        """
        执行耗时操作，并在执行过程中手动更新进度条。
        """
        with Progress() as progress:
            task_id = progress.add_task("[green]Processing ", total=self.total_iterations)
            for i in range(self.total_iterations):
                # 模拟耗时操作
                time.sleep(0.1)  # 暂停0.1秒
                # 更新进度条.这行代码的作用是告诉 Progress 跟踪器，指定任务 task_id 的进度向前推进了1个单位。
                progress.update(task_id, advance=1)
                # 在这里可以添加你的业务逻辑

# 使用示例
if __name__ == "__main__":
    task = TimeConsumingTask(total_iterations=100)
    task.execute()
