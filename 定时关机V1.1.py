import _thread,time,sys,pygame
import pyautogui as pag
import random,os,win32,win32api,win32con
from pykeyboard import PyKeyboard
def 显示时间():
    k = PyKeyboard()
    k.press_key(k.windows_l_key)
    k.tap_key('d')
    k.release_key(k.windows_l_key)
    time.sleep(0.1)
    for i in range(2):
        k.press_key(k.windows_l_key)
        k.release_key(k.windows_l_key)
        time.sleep(0.3)
def time_win(self,占位):
    a = win32api.MessageBox(0, "\n已到达预定关机时间\n\n是否关机? ", "关机提示",win32con.MB_YESNO)
    return a
i = 0
b = True
x, y = pag.position()
while True:
    tempx ,tempy = pag.position()
    Now = time.strftime('%H:%M:%S',time.localtime()).split(':')
    if tempx == x and y == tempy:
        i += 1
    else:
        i = 0
        x, y = pag.position()
    if i > 600:
        if int(Now[0]) == 16 and int(Now[1]) >= 15 and int(Now[2]) >= 00:
            显示时间()
            pygame.mixer.init()
            file = 'C:\Windows\Media\Windows Background.wav'
            m = pygame.mixer.Sound(file)
            m.set_volume(1)
            m.play()
            a = time_win(None,None)
            for i in range(3):
                tempx ,tempy = pag.position()
                if tempx != x and y != tempy:
                    b = False
                    break
                time.sleep(1)
            if b == True and a == 6:
                os.system('shutdown -s -f -t 5')
                time.sleep(1)
                sys.exit()
            elif a == 7:
                win32api.MessageBox(0, "程序已退出...", "退出成功",win32con.MB_OK)
                sys.exit()
        elif int(Now[0]) > 16:
            显示时间()
            pygame.mixer.init()
            file = 'C:\Windows\Media\Windows Background.wav'
            m = pygame.mixer.Sound(file)
            m.set_volume(1)
            m.play()
            a = time_win(None,None)
            if b == True and a == 6:
                os.system('shutdown -s -f -t 5')
                time.sleep(1)
                sys.exit()
            elif a == 7:
                win32api.MessageBox(0, "程序已退出...", "退出成功",win32con.MB_OK)
                sys.exit()
    time.sleep(0.1)
    b = True
