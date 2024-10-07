import random
import os
from time import sleep

for i in range(20):
    try:
        a = 'color '
        l = random.randint(0, 9)
        m = random.randint(0, 9)
        a += f"{l}{m}"
        
        # 使用 subprocess 而不是 system 来提高安全性
        from subprocess import call
        call(a, shell=True)
        
        print(a + '\n' * 5)  # 减少空行数量
        sleep(0.5)
    except Exception as e:
        print(f"发生错误: {e}")