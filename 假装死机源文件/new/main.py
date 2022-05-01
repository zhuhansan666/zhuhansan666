import pygame,time,random,os,win32gui,win32con,win32com
pygame.init()
i = 0
def 活动窗口(hwnd):
    try:
        win32com.client.Dispatch("WScript.Shell").SendKeys('%')
        win32gui.SetForegroundWindow(hwnd)
    except Exception:
        pass
def Window_print(Title,x,y,Size=72):
        font =  pygame.font.SysFont('microsoft Yahei',Size)
        surface = font.render(Title,True,(255,255,255))
        Window.blit(surface,(x,y))
def 置顶(self, hwnd):
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOOWNERZORDER | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
def 取消置顶(self,hwnd):
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                              win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
pygame.mouse.set_visible(False)
pygame.display.set_caption("")
Window = pygame.display.set_mode(flags=pygame.FULLSCREEN|pygame.NOEVENT|pygame.NOFRAME)
h = pygame.display.get_wm_info()['window']
置顶(None,h)
get_dic = Window.get_size()
get_x = get_dic[0]
get_y = get_dic[1]

lowTime = time.time()
ran = 0
ranTime = (random.random()*abs(ran/4.5))

while True:
    while abs(time.time() - lowTime) < abs(ranTime):
        try:
            startMuH = win32gui.FindWindow(None,'搜索') #开始菜单pid
            win32gui.PostMessage(startMuH,win32con.WM_CLOSE) #发送关闭
        except:
            pass
        try:
            rwqhH = win32gui.FindWindow(None,"任务切换") #任务切换(alt+tab)pid
            win32gui.PostMessage(rwqhH,win32con.WM_CLOSE) #发送关闭
        except:
            pass
        try:
            tempH = win32gui.FindWindow(None,"任务视图")
            win32gui.PostMessage(tempH,win32con.WM_CLOSE) #发送关闭
        except:
            pass
        try:
            tempH = win32gui.FindWindow(None,"")
            win32gui.PostMessage(tempH,win32con.WM_CLOSE) #发送关闭
        except:
            pass
        h = pygame.display.get_wm_info()['window']
        置顶(None,h)
        活动窗口(h)
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
        if i >= 10:
            ran = random.randint(3,11)
        else:
            ran = random.randint(6,11)
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
        lowTime = time.time()
        ranTime = (random.random()*abs(ran/4.5))
        pygame.display.update()

i_ = 1000
n = 3
while True:
    try:
        h = pygame.display.get_wm_info()['window']
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
try:
    vid = pygame.image.load('./vid/1887.png')
    vid = pygame.transform.scale(vid,(get_x,get_y))
    Window.blit(vid,(0,0))
    pygame.display.update()
except:
    pass
time.sleep(0.3)
pygame.quit()
