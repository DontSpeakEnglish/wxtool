import random
import os
from time import sleep

def ss():
    try:
        a = 'color '
        l = random.randint(0, 9)
        m = random.randint(0, 9)
        a += f"{l}{m}"
        
        # 使用 subprocess 而不是 system 来提高安全性
        from subprocess import call
        call(a, shell=True)
    except Exception as e:
        print(f"发生错误: {e}")
            
def wechat_xw(e):
    if str(e) == "(1400, 'SetWindowPos', '无效的窗口句柄。')":
        for i in range(15):
            os.system('cls')
            print("未识别到有效微信窗口")
            print("请检查是否已打开并登录微信")
            ss()
            sleep(0.3)
            
    else:
        for i in range(10):
            print(f"发生错误: {e}")
            system('color 0b')
    ei = input("按回车退出...")
    exit()
        
    