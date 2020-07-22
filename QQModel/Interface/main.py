from tkinter import Tk

from QQModel.Interface.login import LoginPage
# 主程序
if __name__ == '__main__':
  root = Tk()
  LoginPage(root)
  root.mainloop()