import threading
import time

# run函数
def run():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 输出当地时间
    timer = threading.Timer(1, run)  # 设置一个定时器，循环输出时间
    timer.start()  # 启动线程

run()