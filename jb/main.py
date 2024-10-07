from os import system
from sys import *
from wxauto import WeChat
from cw import *

def wechat():
    try :
        wx = WeChat()
    except Exception as e:
        wechat_xw(e)
        
    print("已打开微信")
    pipe = r'\\.\pipe\wechat'
    os.mkfifo(pipe)
    with open(pipe, 'w') as f:
        f.write('y'):
    ei = input('按回车关闭窗口...')
    exit()
wechat()