import os
import time
import cv2
import numpy as np
import random
os.system("adb_server connect 127.0.0.1:7555")


def feat():
   
    while (1):#上人开战
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[310,410]==[41,218,178]).all() and 
            (img[310,540]==[30,217,180]).all() and 
            (img[400,400]==[44,209,170]).all() ):
            break  
    if ((img[40,1200]==[16,16,165]).all()):
        x = random.randint(1200,1220)
        y = random.randint(30,55)
        os.system("adb_server shell input tap " + str(x) + " " + str(y))
    xa = random.randint(390,490)
    ya = random.randint(600,640)
    xb = random.randint(610,690)
    yb = random.randint(380,430)
    os.system("adb_server shell input swipe " + str(xa) + " " + str(ya)+ " " + str(xb)+ " " + str(yb))
    time.sleep(random.randint(1,100)/100)
    x = random.randint(580,860)
    y = random.randint(710,740)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(20)
    
    
    
    while (1):#结算
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")    
        if ((img[75,160]==[14,24,207]).all() and 
            (img[151,295]==[255,215,0]).all() and 
            (img[396,169]==[255,177,0]).all() ):
            break 
    time.sleep(3)
    x = random.randint(100,1300)
    y = random.randint(150,400)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)
    
    while (1):
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")    
        if ((img[75,160]==[14,24,207]).all() and 
            (img[154,446]==[252,193,0]).all() and 
            (img[195,535]==[18,226,2]).all() ):
            break 
    time.sleep(3)
    x = random.randint(100,1300)
    y = random.randint(150,400)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)
    
    while (1):
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")    
        if ((img[75,160]==[14,24,207]).all() and 
            (img[169,453]==[248,197,35]).all() and 
            (img[300,453]==[250,199,6]).all() ):
            break 
    time.sleep(3)
    x = random.randint(100,1300)
    y = random.randint(150,400)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)
    
    

while (1):
    
    
    while (1):#选关
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[234,1134]==[230,247,255]).all() and 
            (img[425,1260]==[18,18,18]).all() and 
            (img[610,942]==[146,161,185]).all() ):
            break
    time.sleep(0.5)
    x = random.randint(900,1300)
    y = random.randint(500,600)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)
    
    
    while (1):#进入选协战
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[75,715]==[227,221,177]).all() and 
            (img[517,1265]==[81,133,168]).all() and 
            (img[695,300]==[170,168,162]).all() ):
            break
    time.sleep(0.5)
    x = random.randint(75,340)
    y = random.randint(650,775)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)        

    while (1):#选协战
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[116,568]==[226,250,255]).all() and 
            (img[452,485]==[255,255,255]).all() and 
            (img[36,240]==[243,167,254]).all() ):
            break
    time.sleep(2)
    x = random.randint(750,1300)
    y = random.randint(150,280)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1)   
    x = random.randint(1050,1300)
    y = random.randint(750,785)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(random.randint(1,100)/100) 
        
    while (1):#出击
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[75,715]==[227,221,177]).all() and 
            (img[517,1265]==[81,133,168]).all() and 
            (img[709,353]==[230,247,255]).all() ):
            break
    time.sleep(0.5)
    x = random.randint(960,1300)
    y = random.randint(740,780)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)
    
    while (1):#1战
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[350,950]==[65,147,79]).all() and 
            (img[520,600]==[32,197,122]).all() and 
            (img[600,1150]==[35,65,17]).all() ):
            break
    time.sleep(3)
    x = random.randint(420,540)
    y = random.randint(600,640)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)  
    
    feat()
    
    while (1):#2战
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[517,800]==[23,164,89]).all() and 
            (img[450,1120]==[65,161,101]).all() and 
            (img[240,940]==[[65,160,101]]).all() ):
            break
    time.sleep(0.5)
    x = random.randint(570,700)
    y = random.randint(600,680)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)  
    
    feat()
    
    while (1):#吃药
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[412,642]==[21,161,87]).all() and 
            (img[312,790]==[35,183,109]).all() and 
            (img[316,947]==[62,152,93]).all() ):
            break   
    time.sleep(0.5)
    x = random.randint(270,390)
    y = random.randint(480,560)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)

    while (1):#3战
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[315,800]==[30,187,121]).all() and 
            (img[315,940]==[28,184,110]).all() and 
            (img[315,1080]==[70,144,86]).all() ):
            break   
    time.sleep(0.5)
    x = random.randint(1300,1400)
    y = random.randint(280,340)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)    

    feat()   
    
    while (1):#4战
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[315,650]==[36,176,110]).all() and 
            (img[315,800]==[26,158,92]).all() and 
            (img[415,800]==[24,164,98]).all() ):
            break   
    time.sleep(0.5)
    x = random.randint(1010,1100)
    y = random.randint(190,250)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)  

    feat() 

    while (1):#结算
        os.system("adb_server shell screencap -p /sdcard/1.png")
        os.system("adb_server pull /sdcard/1.png")
        time.sleep(0.5)
        img = cv2.imread("1.png")
        if ((img[205,404]==[0,197,255]).all() and 
            (img[218,718]==[0,205,255]).all() and 
            (img[444,412]==[239,209,85]).all() ):
            break   
    time.sleep(0.5)
    x = random.randint(100,1300)
    y = random.randint(150,400)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)
    x = random.randint(650,670)
    y = random.randint(590,600)
    os.system("adb_server shell input tap " + str(x) + " " + str(y))
    time.sleep(1+random.randint(1,100)/100)       