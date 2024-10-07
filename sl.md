wxtool 思路:
    
    gui界面: godot
    主程序: python 

进入界面:
    
    判断是否为道次进入:

        首次进入：
            运行python程序，调出记事本展示介绍txt文件
            在user://目寻创建文件记录信息
    
        不是首次进入：
            查看user://目录下信息文件不放出介绍项是否为true
        
            true:
               pass

            false:
               (一般情况下不会为false，既然用户大赞周章，就让他看)
               运行python程序，调出记事本展示介绍txt文件
           

