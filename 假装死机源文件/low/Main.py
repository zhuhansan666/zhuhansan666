import pygame,time,random,os
import win32gui, win32con
pygame.init()
i = 0
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
def SysFont(name, size, bold=False, italic=False, constructor=None):
    pass
def render(self, text, antialias, color, background=None):
    pass
def Window_print(Title,x,y,Size=72):
        font =  pygame.font.SysFont('microsoft Yahei',Size)
        surface = font.render(Title,False,(255,255,255))
        Window.blit(surface,(x,y))
pygame.mouse.set_visible(False)
pygame.display.set_caption("None")
Window = pygame.display.set_mode()
h = 获取曲柄('None')
置顶(None,h)
get_dic = Window.get_size()
get_x = get_dic[0]
get_y = get_dic[1]
while True:
    h = 获取曲柄('None')
    置顶(None,h)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass
    if i == 0:
        i = 1
        pic = pygame.image.load('./pic/蓝屏.png')
        pic = pygame.transform.scale(pic,(get_x,get_y))
        Window.blit(pic,(0,0))
        size = round(get_x/35)
        if size < 0:
            size = 72
        Window_print('{}'.format('%02d'%i),get_x*0.2219,get_y*0.475,size)
        Window_print('% 完成',get_x*0.26,get_y*0.475,size)
        pygame.display.update()
        time.sleep(random.random()*1.3)
    else:
        ran = random.randint(0,11)
        if i >= 100:
            i = 100
        elif i % 4 == 1:
            i = i + ran
            if i >= 100:
                i = 100
        else:
            i = i + 1
        pic = pygame.image.load('./pic/蓝屏.png')
        pic = pygame.transform.scale(pic,(get_x,get_y))
        Window.blit(pic,(0,0))
        size = round(get_x/35)
        if size < 0:
            size = 72
        Window_print('{}'.format('%02d'%i),get_x*0.2219,get_y*0.475,size)
        if i == 100:
            Window_print('% 完成',get_x*0.279,get_y*0.475,size)
            break
        else:
            Window_print('% 完成',get_x*0.26,get_y*0.475,size)
        pygame.display.update()
        time.sleep(random.random()*(ran/4.5))
i_ = 1000
n = 3
while True:
    try:
        h = 获取曲柄('None')
        置顶(None,h)
        Window = pygame.display.set_mode()
        vid = pygame.image.load('./vid/{}.png'.format(i_))
        vid = pygame.transform.scale(vid,(get_x,get_y))
        Window.blit(vid,(0,0))
        pygame.display.update()
        i_ = i_ + n
    except:
        break
    if i_ > 1710 and i_ < 1882:
        n = 4
vid = pygame.image.load('./vid/1887.png')
vid = pygame.transform.scale(vid,(get_x,get_y))
Window.blit(vid,(0,0))
pygame.display.update()
time.sleep(0.5)
pygame.quit()