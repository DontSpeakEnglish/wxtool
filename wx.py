from wxauto import WeChat #引入微信回复模块
import pyautogui as d #用于进行键盘操作
import time #引入时间模块

def send_msg(msg):
    """
    发送消息函数，通过模拟键盘操作发送微信消息。
    
    参数:
    msg: str,要发送的消息内容。
    
    该函数首先调用wx.SendMsg函数,向指定的接收者发送消息内容。
    随后,通过模拟按下并释放Tab键,以及按下并释放Enter键来完成消息的发送操作。
    这里的键盘操作模拟是为了在特定的应用程序界面中执行消息发送流程。
    """
    wx.SendMsg(msg, who)
    d.keyDown('Tab')
    d.keyUp('Tab') #选择'发送'控件
    d.keyDown('Enter')
    d.keyUp('Enter') #发送消息

def Feedback(news, conidttion, msg, frequency):
    """
    反馈函数，用于处理收到的消息。
    
    参数:
    news: str,收到的消息内容。
    conidttion: str,触发回复内容。
    msg: str,要回复的消息内容。
    frequency: int,回复的次数。
    
    该函数首先判断收到的消息是否是特定内容。
    如果包含,则调用send_msg函数回复指定的消息内容。
    """
    if news == conidttion:
        print('收到消息：', news)
        for i in range(frequency):
            send_msg(msg)
            print('已回复：', msg)

wx = WeChat()
who = 'xxx'
wx.AddListenChat(who=who)   
frequency = 20


while True:
    msgs = wx.GetListenMessage()
    time.sleep(1)
    if msgs != {}:
        for name in msgs: #遍历所有消息
            msg = msgs[name] #获取字典的键
            msg = msg[0]
            msg = msg[1]  #获取消息内容
            Feedback(msg, 'ggb最帅', '死猪', frequency)
