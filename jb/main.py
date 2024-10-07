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
    ei = input('按回车关闭窗口...')
    exit()
wechat()