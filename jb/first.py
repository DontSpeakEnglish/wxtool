from os import path, system

file_path = r'jb\js.txt'

if path.exists(file_path):
    system(f'notepad {file_path}')
    ei = input("按回车关闭此窗口...")
    
else:
    print(f"文件 {file_path} 不存在。")

