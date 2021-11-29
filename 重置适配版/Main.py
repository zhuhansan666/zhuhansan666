import pygame,sys,random,os,win32api,win32con
from time import sleep as de
from pygame.constants import K_ESCAPE, K_LALT, K_RALT, K_SPACE, KEYDOWN, KEYUP, QUIT ,K_LEFT ,K_RIGHT
pygame.init()
b = False
low_list = []
get = pygame.display.set_mode()
get_x = get.get_size()[0]
get_y = get.get_size()[1]
low_list_size = round(get_x/35.5)
get.fill((255,255,255))
def Get_print(Title,x,y,color=(0,0,0),Size=round(get_x/35.5)):
        font =  pygame.font.SysFont('microsoft Yahei',Size)
        surface = font.render(Title,True,color)
        get.blit(surface,(x,y))
def Window_print(Title,x,y,color=(0,0,0),Size=round(get_x/35.5)):
        font =  pygame.font.SysFont('microsoft Yahei',Size)
        surface = font.render(Title,True,color)
        window.blit(surface,(x,y))
pygame.display.update()
# while b == False:
#     Get_print('什么？不会使用？来看看教程吧 Click Here (点击空白处关闭)', get_x*0.1, get_y*0.4)
#     pygame.display.update()
#     for e in pygame.event.get():
#         if e.type == pygame.MOUSEBUTTONDOWN and e.pos[0] > get_x*0.1 and e.pos[0] < get_x*0.9 and e.pos[1] > get_y*0.4 and e.pos[1] < get_y*0.53:
#             os.system('explorer "https://www.bilibili.com/video/BV1YS4y1R7mD?t=0"')
#             pygame.quit()
#             sys.exit()
#         if e.type == pygame.MOUSEBUTTONDOWN:
#             b = True
#             break
Mes = win32api.MessageBox(0, "什么？不会使用？来看看教程吧", "教程看查",win32con.MB_YESNOCANCEL)
if Mes == 6:
    os.system('explorer "https://www.bilibili.com/video/BV1YS4y1R7mD?t=0"')
    pygame.quit()
    sys.exit()
elif Mes == 2:
    pygame.quit()
    sys.exit()
window = pygame.display.set_mode((get_x,get_y-40))
window.fill((255,255,255))
j1 = (get_x*0.1,get_y*0.8,get_x*0.19,get_y*0.13)
j2 = (get_x*0.4,get_y*0.798,get_x*0.19,get_y*0.13)
j3 = (get_x*0.73,get_y*0.798,get_x*0.19,get_y*0.13)
pygame.draw.rect(window,(0,0,0),j1,round((get_x/102.4)*0.3))
Window_print('上一个', j1[0]*1.49, j1[1]*1.033)
pygame.draw.rect(window,(0,0,0),j2,round((get_x/102.4)*0.3))
Window_print('退出', j2[0]*1.16, j2[1]*1.037)
pygame.draw.rect(window,(0,0,0),j3,round((get_x/102.4)*0.3))
Window_print('下一个', j3[0]*1.07,j3[1]*1.035)
pygame.display.update()
number = None
def pop_up_box():
    num = None
    import tkinter
    from tkinter import Text,INSERT,END
    def inputint():
        nonlocal num
        global number
        if len(var.get().strip()) < 1 or type(var.get().strip()) != int or var.get().strip().isdisgit() == False:
            text = Text(root, width=50, height=10, undo=True, autoseparators=False)
            text.pack()
            text.insert(INSERT, '输入错误或为空')
        try:
            num = int(var.get().strip())
            root.destroy()
            number = num
        except:
            var.set('')
            num = False
    def inputclear():
        nonlocal num
        var.set('')
        num = 0
    root = tkinter.Tk(className='班级人数输入')
    root.geometry('270x100')
    var = tkinter.StringVar()
    var.set('')
    entry1 = tkinter.Entry(root, textvariable=var)
    entry1.pack()
    btn1 = tkinter.Button(root, text='确认', command=inputint)
    btn2 = tkinter.Button(root, text='清除', command=inputclear)
    btn2.pack(side='right')
    btn1.pack(side='right')
    text = Text(root, width=50, height=10, undo=True, autoseparators=False)
    text.pack()
    text.insert(INSERT, '请在上方输入框中输入班级人数')
    root.mainloop()
pop_up_box()
def New_list():
    global r,run_number,number
    students_list = []
    r = number
    run_number = r
    if not type(run_number) == int:
        pygame.quit()
        sys.exit()
    for i in range(run_number):
        students_list.append(i+1)
    return students_list
students_list = New_list()
while True:
    if len(students_list) < 1:
        for i in range(3):
            pygame.draw.rect(window,(255,255,255),(1,1,get_x,get_y*0.7),0)
            Window_print('所有学生抽人完毕 将在 {} 秒后退出.'.format(2-i),get_x*0.2,get_y*0.35,Size=round(get_x/25))
            Window_print('涛哥的随机抽人程序',get_x*0.27,get_y*0.1,Size=round(get_x/20))
            pygame.display.update()
            de(1)
        Mes2 =  win32api.MessageBox(0, '小主我已经帮你随机了{}名学生了,要不去github上看看源码?'.format(run_number), "提示",win32con.MB_YESNO)
        if Mes2 == 6:
            os.system('explorer "https://github.com/zhuhansan666/zhuhansan666/blob/main/%E9%87%8D%E7%BD%AE%E9%80%82%E9%85%8D%E7%89%88/Main.py"')
        pygame.quit()
        sys.exit()
    wait = True
    Window_print('涛哥的随机抽人程序',get_x*0.27,get_y*0.1,Size=round(get_x/20))
    now = students_list[random.randint(0, r-1)]
    students_list.remove(now)
    r = r - 1
    Window_print('已抽'+str(low_list),get_x*0.2 , get_y*0.25,Size=low_list_size)
    Window_print('现在为{}号'.format(now),get_x*0.2,get_y*0.35,Size=round(get_x/30))
    Window_print('剩余{}个'.format(len(students_list)),get_x*0.2,get_y*0.45,Size=round(get_x/30))
    pygame.display.update()
    while wait == True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
            if e.type == pygame.MOUSEMOTION and e.pos[0] > j1[0] and e.pos[0] < (j1[0]+j1[2]) and e.pos[1] > j1[1] and e.pos[1] < (j1[1]+j1[1]):
                pygame.draw.rect(window,(192,192,192),j1,0)
                Window_print('上一个', j1[0]*1.49, j1[1]*1.033)
                pygame.display.update()
            else:
                pygame.draw.rect(window,(255,255,255),j1,0)
                Window_print('上一个', j1[0]*1.49, j1[1]*1.033)
                pygame.draw.rect(window,(0,0,0),j1,round((get_x/102.4)*0.3))
            if e.type == pygame.MOUSEBUTTONDOWN and e.pos[0] > j1[0] and e.pos[0] < (j1[0]+j1[2]) and e.pos[1] > j1[1] and e.pos[1] < (j1[1]+j1[1]):
                pygame.draw.rect(window,(192,192,192),j1,0)
                Window_print('上一个', j1[0]*1.49, j1[1]*1.033)
                Window_print('暂不支持此功能.', 1, 1)
                pygame.display.update()
                de(0.1)
            if e.type == pygame.MOUSEMOTION and e.pos[0] > j2[0] and e.pos[0] < (j2[0]+j2[2]) and e.pos[1] > j2[1] and e.pos[1] < (j2[1]+j2[1]):
                pygame.draw.rect(window,(192,192,192),j2,0)
                Window_print('退出', j2[0]*1.16, j2[1]*1.037)
                pygame.display.update()
            if e.type == pygame.MOUSEBUTTONDOWN and e.pos[0] > j2[0] and e.pos[0] < (j2[0]+j2[2]) and e.pos[1] > j2[1] and e.pos[1] < (j2[1]+j2[1]):
                pygame.draw.rect(window,(192,192,192),j2,0)
                for i in range(3):
                    pygame.draw.rect(window,(255,255,255),(1,1,get_x,get_y*0.7),0)
                    pygame.draw.rect(window,(0,0,0),j2,round((get_x/102.4)*0.3))
                    Window_print('退出', j2[0]*1.16, j2[1]*1.037)
                    Window_print('退出 将在{}秒后退出.'.format(2-i), get_x*0.2,get_y*0.35,)
                    Window_print('涛哥的随机抽人程序',get_x*0.27,get_y*0.1,Size=round(get_x/20))
                    pygame.display.update()
                    de(1)
                pygame.quit()
                sys.exit()
            else:
                pygame.draw.rect(window,(255,255,255),j2,0)
                Window_print('退出', j2[0]*1.16, j2[1]*1.037)
                pygame.draw.rect(window,(0,0,0),j3,round((get_x/102.4)*0.3))
            if e.type == pygame.MOUSEMOTION and e.pos[0] > j3[0] and e.pos[0] < (j3[0]+j3[2]) and e.pos[1] > j3[1] and e.pos[1] < (j3[1]+j3[1]):
                pygame.draw.rect(window,(192,192,192),j3,0)
                Window_print('下一个', j3[0]*1.07,j3[1]*1.035)
                pygame.display.update()
            if e.type == pygame.MOUSEBUTTONDOWN and e.pos[0] > j3[0] and e.pos[0] < (j3[0]+j3[2]) and e.pos[1] > j3[1] and e.pos[1] < (j3[1]+j3[1]):
                pygame.draw.rect(window,(0,0,0),j3,round((get_x/102.4)*0.3))
                pygame.draw.rect(window,(192,192,192),j3,0)
                Window_print('下一个', j3[0]*1.07,j3[1]*1.035)
                Window_print('下一个', 1,1)
                pygame.display.update()
                de(0.1)
                low_list.append(now)
                wait = False
            else:
                pygame.draw.rect(window,(255,255,255),j3,0)
                pygame.draw.rect(window,(0,0,0),j3,round((get_x/102.4)*0.3))
                Window_print('下一个', j3[0]*1.07,j3[1]*1.035)
            if e.type == pygame.MOUSEMOTION and e.pos[1] < get_y*0.79:
                pygame.draw.rect(window,(0,0,0),j1,round((get_x/102.4)*0.3))
                Window_print('上一个', j1[0]*1.49, j1[1]*1.033)
                pygame.draw.rect(window,(0,0,0),j2,round((get_x/102.4)*0.3))
                Window_print('退出', j2[0]*1.16, j2[1]*1.037)
                pygame.draw.rect(window,(0,0,0),j3,round((get_x/102.4)*0.3))
                Window_print('下一个', j3[0]*1.07,j3[1]*1.035)
                pygame.display.update()
    pygame.draw.rect(window,(255,255,255),(1,1,get_x,get_y*0.79),0)
    low_list_size = round((get_x/35.5)-((get_x/35.5)*(len(low_list)/run_number/1.57)))