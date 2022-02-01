import subprocess,sys
from tkinter import Tk
from tkinter.messagebox import *
import time,os

from writeReg import write_reg
write_reg('室内操')

root = Tk()
root.withdraw()
gx = root.winfo_screenwidth()
gy = root.winfo_screenheight()


file = sys.argv[0]
if '\\' in file:
    file = file.replace(file.split('\\')[-1],'')
elif '/' in file:
    file = file.replace(file.split('/')[-1],'')

# _f_ = __file__
# if '\\' in _f_:
#     _f_ = _f_.replace(_f_.split('\\')[-1],'')
# elif '/' in _f_:
#     _f_ = _f_.replace(_f_.split('/')[-1],'')


maincmd = f'"{file}ffplay/ffplay.exe" -x {gx} -y {gy} -autoexit -fs -window_title "室内操播放" -loglevel quiet -i "{file}学校室内课间操.mp4"'
# w1 = '''<h1>即将播放室内操视频，请不要关闭即将弹出的CMD窗口，因为本程序使用了开源播放器: ffplay(ffmpeg)，无法避免地弹出了运行窗口.</h1>'''
# wcmd = f'{_f_}main.html'


def main():
    # try:
    #     with open(f'{_f_}main.html','w+',encoding='utf-8') as f:
    #         f.write(w1)
    #     os.startfile(wcmd)
    #     time.sleep(5)
    # except:
    #     pass
    subprocess.Popen(maincmd)

while True:
    Now_h = int(time.strftime('%H',time.localtime()))
    Now_m = int(time.strftime('%M',time.localtime()))
    if Now_h == 8 and Now_m >= 00 and Now_m <= 30:
        main()
        break
    if Now_h >= 8 or Now_h == 8 and Now_m >= 31:
        showinfo('退出提示','时间超过 8:30\n按下"确定"键退出...\n')
        break
    time.sleep(0.5)
