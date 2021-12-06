import pygame,random,os
from time import sleep as de
pygame.init()
w = pygame.display.set_mode()
pygame.display.set_caption('Main')
pygame.mouse.set_visible(False)
import win32gui, win32con,win32com,win32com.client
def keypass_esc(num=1,wait=0.0):
    shell = win32com.client.Dispatch("WScript.Shell")
    for i in range(num):
        shell.SendKeys('{ESC}')
        if not wait == 0:
            time.sleep(wait)
def 置顶(self, hwnd):
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOOWNERZORDER | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
def 取消置顶(self,hwnd):
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                              win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
def 获取曲柄(title):
    hwnd_title = dict()
    def get_all_hwnd(hwnd,mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h,t in hwnd_title.items():
        if t == title:
            return h
def 设置活动窗口(hwnd):
    win32gui.BringWindowToTop(hwnd)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)
while True:
    import win32gui, win32con,win32com,win32com.client
    h = 获取曲柄('Main')
    置顶(None, h)
    pygame.mouse.set_visible(False)
    w.fill((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pass
        if e.type == pygame.KEYDOWN and e.key == 1073742051:
            keypass_esc()
        if e.type == 770:
            keypass_esc(num=3)
        try:
            h = 获取曲柄('Main')
            设置活动窗口(h)
        except:
            pass
