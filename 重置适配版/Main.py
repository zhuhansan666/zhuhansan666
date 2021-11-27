import pygame,sys,random,os
from time import sleep as de
from pygame.constants import K_ESCAPE, K_LALT, K_RALT, K_SPACE, KEYDOWN, KEYUP, QUIT ,K_LEFT ,K_RIGHT
pygame.init()
b = False
get = pygame.display.set_mode()
get_x = get.get_size()[0]
get_y = get.get_size()[1]
get.fill((255,255,255))
def SysFont(name, size, bold=False, italic=False, constructor=None):
    pass
def render(self, text, antialias, color, background=None):
    pass
def Get_print(Title,x,y,color=(0,0,0),Size=72):
        font =  pygame.font.SysFont('microsoft Yahei',Size)
        surface = font.render(Title,True,color)
        get.blit(surface,(x,y))
def Window_print(Title,x,y,color=(0,0,0),Size=72):
        font =  pygame.font.SysFont('microsoft Yahei',Size)
        surface = font.render(Title,True,color)
        window.blit(surface,(x,y))
while b == False:
    Get_print('什么？不会使用？来看看教程吧 Click Here (点击空白处关闭)', get_x*0.1, get_y*0.4)
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN and e.pos[0] > get_x*0.1 and e.pos[0] < get_x*0.9 and e.pos[1] > get_y*0.4 and e.pos[1] < get_y*0.53:
            os.system('explorer "https://www.bilibili.com/video/BV1YS4y1R7mD?t=0"')
            pygame.quit()
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            b = True
            break
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
def New_list():
    global r
    students_list = []
    try:
        with open('n.txt','r') as f:
            r = f.read()
            if ':' in r:
                r = r.split('人数:')[1]
            elif '：' in r:
                r = r.split('人数：')[1]
            r = int(r)
    except:
        try:
            with open('n.txt','w+') as f:
                f.write('人数:45')
            r = 45
        except PermissionError :
            for i in range(3):
                pygame.draw.rect(window,(255,255,255),(1,1,get_x,get_y*0.7),0)
                pygame.draw.rect(window,(0,0,0),j2,round((get_x/102.4)*0.3))
                Window_print('退出', j2[0]*1.16, j2[1]*1.037)
                Window_print('错误：文件未生成成功 因为无管理员权限 请退出以"管理员身份运行"重试', get_x*0.05, get_y*0.45,Size=round(get_x/40))
                Window_print('退出 将在{}秒后退出.'.format(2-i), get_x*0.2,get_y*0.35,)
                Window_print('涛哥的随机抽人程序',get_x*0.27,get_y*0.1,Size=round(get_x/20))
                pygame.display.update()
                de(1)
            pygame.quit()
            sys.exit()
    if r < 1:
        r = 45
        try:
            with open('n.txt','w+') as f:
                f.write('人数:45')
            r = 45
        except PermissionError :
            for i in range(3):
                pygame.draw.rect(window,(255,255,255),(1,1,get_x,get_y*0.7),0)
                pygame.draw.rect(window,(0,0,0),j2,round((get_x/102.4)*0.3))
                Window_print('退出', j2[0]*1.16, j2[1]*1.037)
                Window_print('错误：文件未生成成功 因为无管理员权限 请退出以"管理员身份运行"重试', get_x*0.05, get_y*0.45,Size=round(get_x/40))
                Window_print('退出 将在{}秒后退出.'.format(2-i), get_x*0.2,get_y*0.35,)
                Window_print('涛哥的随机抽人程序',get_x*0.27,get_y*0.1,Size=round(get_x/20))
                pygame.display.update()
                de(1)
            pygame.quit()
            sys.exit()
    run_number = r
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
        pygame.quit()
        sys.exit()
    wait = True
    Window_print('涛哥的随机抽人程序',get_x*0.27,get_y*0.1,Size=round(get_x/20))
    now = students_list[random.randint(0, r-1)]
    students_list.remove(now)
    r = r - 1
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