import pygame,sys,os,time,json,winreg
import tkinter
from tkinter.messagebox import *

window = tkinter.Tk()
window.withdraw()  # 退出默认 tk 窗口

pygame.init()

clock = pygame.time.Clock()

def restart():
    # python = sys.executable
    # os.execl(python, python, * sys.argv)
    os.startfile(sys.argv[0])

def Window_print(Title,x,y,name,color=(0,0,0),Size=72,tmd=255): #可改透明度（tmd参数）
		font =  pygame.font.SysFont('microsoft Yahei',Size)
		surface = font.render(Title,True,color)
		surface.set_alpha(tmd)
		name.blit(surface,(x,y))
		return surface.get_size()
def w_m_print(Title,x,y,name,maxx:int=None,color=(0,0,0),Size=72,tmd=255):
        if x == 'm':
                get_x = maxx
                font =  pygame.font.SysFont('microsoft Yahei',Size)
                surface = font.render(Title,True,color)
                surface.set_alpha(tmd)
                getx,gety = surface.get_size()
                name.blit(surface,(get_x*0.5-round(getx/2),y))
        else:
                font =  pygame.font.SysFont('microsoft Yahei',Size)
                surface = font.render(Title,True,color)
                surface.set_alpha(tmd)
                name.blit(surface,(x,y))
def time_check(_time_:str,精确匹配:bool=False):
    '''时间格式:%Y-%m-%d %H:%M:%S'''
    try:
        timeStamp = float(time.mktime(time.strptime(_time_, "%Y-%m-%d/%H:%M:%S")))
    except:
        return "错误:时间格式问题"
    cache = timeStamp-time.time()
    if 精确匹配:
        if round(cache,3) <= 0.0:
            return (00,00,00,00,000,True)
        else:
            d = int(cache // 86400)
            H = int((cache - d*86400) // 3600)
            M = int((cache - d*86400 - H*3600) // 60)
            S = int((cache - d*86400 - H*3600 - M*60))
            MS = (cache % 1) * 1000
            return ('%02d'%d,'%02d'%H,'%02d'%M,'%02d'%S,'%03d'%MS,False)
    elif not 精确匹配:
        if cache <= 0.0:
            return (00,00,00,00,000,True)
        else:
            d = int(cache // 86400)
            H = int((cache - d*86400) // 3600)
            M = int((cache - d*86400 - H*3600) // 60)
            S = int((cache - d*86400 - H*3600 - M*60))
            MS = (cache % 1) * 1000
            return ('%02d'%d,'%02d'%H,'%02d'%M,'%02d'%S,'%03d'%MS,False)
import ctypes
def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

def check_ini(rootfile:str,filename:str,info:str="TurnOnAutoStart = False\nMaiTextSize = auto\n"):
    if rootfile[-1] == '\\' or  rootfile[-1] == '/':
        _file_ = os.path.exists("{}{}.ini".format(rootfile,filename))
    else:
        _file_ = os.path.exists("{}/{}.ini".format(rootfile,filename))
    if not _file_:
        try:
            with open('{}.ini'.format(filename),'w+',encoding='utf-8') as f:
                f.write(info)
            return info.split('\n')
        except PermissionError:
            if is_admin():
                with open('{}.ini'.format(filename),'w+',encoding='utf-8') as f:
                    f.write(info)
                return info.split('\n')
            else:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
                sys.exit(0)
    else:
        try:
            with open('{}.ini'.format(filename),'r+',encoding='utf-8') as f:
                r = f.readlines()
            return r
        except EOFError as e:
            showerror('错误', '没有预期的错误: {}'.format(e))
            return False

def write_reg(Error=False):
    '''将本文件写入自启动注册表（不受封装限制）'''
    import ctypes,sys,winreg
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    if is_admin():
        key_info = '"{}"'.format(sys.argv[0])
        zcb = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
        key=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,zcb,access=winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key,'autoTurnOFF',0,winreg.REG_SZ,key_info)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        if Error:
            raise SystemError('管理员权限获取失败')
        else:
            sys.exit(2)


file = sys.argv[0]
if '\\' in file:
    file = file.replace(file.split('\\')[-1],'')
elif '/' in file:
    file = file.replace(file.split('/')[-1],'')

r2 = check_ini(file,'配置','实时更新 = False\n配置文件实时更新 = True\nTurnOnAutoStart = False\nMaiTextSize = auto\n')


try:
    with open(file+'times.json',"r+",encoding='utf-8') as f:
        r = f.read()
    if "{" in r and "}" in r:
        r = json.loads(r)
    else:
        with open(file+'times.json',"w+",encoding='utf-8') as f:
            f.write('{"错误":"用户没有定义时间,请删除本内容以继续定义时间"}')
        result = showerror('错误', '用户没有修改\n"{}times.json"\n因为在此之前json文件为空'.format(file))
        os.startfile('"{}times.json"'.format(file))
        sys.exit(0)
except FileNotFoundError:
    try:
        import ctypes
        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
        if is_admin():
            try:
                with open(file+'times.json',"w+",encoding='utf-8') as f:
                    f.write('{"错误":"用户没有定义时间,请删除本内容以继续定义时间"}')
                sys.exit(0)
            except PermissionError:
                result = showerror('错误', "请重启本程序.")
                restart()
                sys.exit(0)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit(0)
    except:
        result = showerror('错误', "请重启本程序.")
        restart()
        sys.exit(0)
except PermissionError:
    if is_admin():
        try:
            with open(file+'times.json',"w+",encoding='utf-8') as f:
                f.write('{"错误":"用户没有定义时间,请删除本内容以继续定义时间"}')
            sys.exit(0)
        except PermissionError:
            result = showerror('错误', "请重启本程序.")
            restart()
            sys.exit(0)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit(0)
except json.decoder.JSONDecodeError:
    result = showerror('错误', "json文件内容错误.")
    os.startfile('"{}times.json"'.format(file))
    sys.exit(0)

# 配置部分_____________________________________


title = '期末考试倒计时 #/* by 涛哥 *\#'
icon = '{}icon.png'.format(file)
mouse = False
find_ico = False

full = True
window = pygame.display.set_mode(flags=pygame.RESIZABLE)
pygame.display.set_caption(title)
try:
    ico = pygame.image.load(icon)
    pygame.display.set_icon(ico)
    find_ico = True
except:
    find_ico = False
window.fill((255,255,255))
pygame.display.flip()
pygame.mouse.set_visible(mouse)


if not find_ico:
    pygame.display.quit()
    result = showwarning('警告', '没有找到图片: "{}"'.format(icon))
    window = pygame.display.set_mode(flags=pygame.RESIZABLE)
    pygame.display.set_caption(title)
    window.fill((255,255,255))
    pygame.display.flip()
    pygame.mouse.set_visible(mouse)


getx,gety = window.get_size()
maxx,maxy = window.get_size()
x,y = round(getx*0.03),round(gety*0.17)
size = getx // 33
fps_size = 20
fps_color = (200,25,30)
fpsx,fpsy = 10,3
cha_x = 0
cha_y = round(size*1.2)
shuiying = '本程序由 涛哥 制作,未经授权禁止私自转载或发布.'
scolor = (0,0,0) 
ssize = getx // 150
sy = gety - round(ssize*1.7)
w_title = '倒计时'
tcolor = (0,0,0) 
tsize = getx // 17
ty = round(tsize*0.1)
time_type = "%Y-%m-%d %H:%M:%S"
fps = 60
f11_pl = 5*fps

# 系统自动配置
pzautoF5 = False
autoF5 = False


for pz in r2:
    if 'MaiTextSize' in pz and '=' in pz:
        pz = str(pz).replace(' ','')
        pz = pz.split('=')[1]
        if not pz == 'auto' and pz.isdigit():
            size = int(pz)
    if 'TurnOnAutoStart' in pz and '=' in pz:
        pz = str(pz).replace(' ','')
        pz = pz.split('=')[1]
        if pz.isalnum() and bool(pz):
            write_reg()
    if '实时更新' in pz and '=' in pz:
        pz = str(pz).replace(' ','')
        pz = pz.split('=')[1]
        if pz.isalnum() and bool(pz):
            autoF5 = True
    if '配置文件实时更新' in pz and '=' in pz:
        pz = str(pz).replace(' ','')
        pz = pz.split('=')[1]
        if pz.isalnum() and bool(pz):
            pzautoF5 = True
# 结束系统自动配置

# 结束配置部分___________________________________

F11 = False
f11n = 0

window = pygame.display.set_mode((maxx,maxy-20),pygame.RESIZABLE)
gety = window.get_height()
sy = gety - round(ssize*1.7)


try:
    if r == {"错误":"用户没有定义时间,请删除本内容以继续定义时间"}:
        pygame.display.quit()
        result = showerror('错误', '用户没有修改\n"{}times.json"'.format(file))
        os.startfile('"{}times.json"'.format(file))
    else:
        raise TypeError
except TypeError:
    while True:
        if pzautoF5:
            r2 = check_ini(file,'配置')
            for pz in r2:
                if 'MaiTextSize' in pz and '=' in pz:
                    pz = str(pz).replace(' ','')
                    pz = pz.split('=')[1]
                    if not pz == 'auto' and pz.isdigit():
                        size = int(pz)
                if 'TurnOnAutoStart' in pz and '=' in pz:
                    pz = str(pz).replace(' ','')
                    pz = pz.split('=')[1]
                    if pz.isalnum() and bool(pz):
                        write_reg()
                if '实时更新' in pz and '=' in pz:
                    pz = str(pz).replace(' ','')
                    pz = pz.split('=')[1]
                    if pz.isalnum() and bool(pz):
                        autoF5 = True
                if '配置文件实时更新' in pz and '=' in pz:
                    pz = str(pz).replace(' ','')
                    pz = pz.split('=')[1]
                    if pz.isalnum() and bool(pz):
                        pzautoF5 = True
        if autoF5:
            with open('{}times.json'.format(file),'r+',encoding='utf-8') as f2:
                r2 = f2.read()
                try:
                    r = json.loads(r2)
                except:
                    pass
        if F11:
            f11n += round(clock.get_fps(),1)
        if f11n > f11_pl:
            f11n = 0
            F11 = False
        getx,gety = window.get_size()
        clock.tick(fps)
        window.fill((255,255,255))
        temp = 1
        for i in r:
            low = str(r[i]).split(',')[0].replace(' ','')
            if ',' in str(r[i]):
                _max = str(r[i]).split(',')[1].replace(' ','')
            else:
                _max = None
            times = time_check(low)
            if times != "错误:时间格式问题":
                d = int(times[0])
                H = int(times[1])
                M = int(times[2])
                S = int(times[3])
                MS = int(times[4])
                now = bool(times[-1])
                if not now:
                    if not now:
                        fx,fy = Window_print('距离{}剩余{}天{}时{}分{}秒{}毫秒'.format(i,'%02d'%d,'%02d'%H,'%02d'%M,'%02d'%S,'%03d'%MS),x+temp*cha_x,y+temp*cha_y,window,Size=size)
                        if x + fx > getx:
                            x -= 1
                        elif x  < 0:
                            x += 1
                        if y + fy > gety:
                            y -= 1
                        elif y < 0:
                            y += 1 
                    elif now:
                        temp -= 1
            else:
                pygame.display.quit()
                result = showerror('错误', '"{}"的开始时间格式存在问题'.format(i))
                import pygame.display
                pygame.display.init()
                if full == True:
                    window = pygame.display.set_mode((maxx,maxy),pygame.FULLSCREEN)
                    window.fill((255,255,255))
                    pygame.display.flip()
                    gety = window.get_height()
                    sy = gety - round(ssize*1.7)
                elif full == False:
                    window = pygame.display.set_mode((maxx,maxy-21),pygame.RESIZABLE)
                    window.fill((255,255,255))
                    pygame.display.flip()
                    gety = window.get_height()
                    sy = gety - round(ssize*2)
            if ',' not in str(r[i]):
                _max = None
            times = ''
            times = time_check(_max)
            if times != "错误:时间格式问题" and now:
                if len(times) < 1:
                    times = time_check(_max)
                d = int(times[0])
                H = int(times[1])
                M = int(times[2])
                S = int(times[3])
                MS = int(times[4])
                now = bool(times[-1])
                if not now:
                    fx,fy = Window_print('距离{}结束剩余{}天{}时{}分{}秒{}毫秒'.format(i,'%02d'%d,'%02d'%H,'%02d'%M,'%02d'%S,'%03d'%MS),x+temp*cha_x,y+temp*cha_y,window,Size=size)
                    if x + fx > getx:
                        x -= 1
                    elif x  < 0:
                        x += 1
                    if y + fy > gety:
                        y -= 1
                    elif y < 0:
                        y += 1 
                elif now:
                    temp -= 1
                elif not now :
                    pass
                elif times != "错误:时间格式问题":
                    pygame.display.quit()
                    result = showerror('错误', '"{}"的结束时间格式存在问题'.format(i))
                    import pygame.display
                    pygame.display.init()
                    if full == True:
                        window = pygame.display.set_mode((maxx,maxy),pygame.FULLSCREEN)
                        window.fill((255,255,255))
                        pygame.display.flip()
                        gety = window.get_height()
                        sy = gety - round(ssize*1.7)
                    elif full == False:
                        window = pygame.display.set_mode((maxx,maxy-21),pygame.RESIZABLE)
                        window.fill((255,255,255))
                        pygame.display.flip()
                        gety = window.get_height()
                        sy = gety - round(ssize*2)
            temp += 1
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYUP and e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)
            if e.type == pygame.KEYUP and e.key == pygame.K_F11 and not F11:
                F11 = True
                if full == False:
                    window = pygame.display.set_mode((maxx,maxy),pygame.FULLSCREEN)
                    window.fill((255,255,255))
                    pygame.display.flip()
                    gety = window.get_height()
                    sy = gety - round(ssize*2)
                    full = True
                elif full == True:
                    window = pygame.display.set_mode((maxx,maxy-21),pygame.RESIZABLE)
                    window.fill((255,255,255))
                    pygame.display.flip()
                    gety = window.get_height()
                    sy = gety - round(ssize*2)
                    full = False
        now_time = time.strftime(time_type,time.localtime())
        w_m_print(now_time,'m',y-(cha_y*0.37),window,getx,Size= getx // 27)
        Window_print(str(round(clock.get_fps(),1)),fpsx,fpsy,window,Size=fps_size,color=fps_color)
        w_m_print(w_title,'m',ty,window,getx,tcolor,tsize)
        w_m_print(shuiying,'m',sy,window,getx,scolor,ssize)
        pygame.display.update()
except:
    pygame.display.quit()
    result = showerror('错误', '"{}times.json"\n创建失败,请将此文件放入无需管理员权限的文件夹运行,谢谢.\n或手动创建"times.json"在"{}"文件夹下.'.format(file,file))
