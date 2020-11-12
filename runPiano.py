#https://virtualpiano.net/?song-post-4800
import pyautogui,time
time.sleep(5)
pyautogui.click(100, 100)
f = open("stilldre.txt", "r")
for j in f:
    i=0
    while(i<len(j)):
        time.sleep(0.08)
        if(j[i]=='['):
            s=''
            while(j[i]!=']'):
                i+=1
                s+=j[i]
            if(len(s)==1):
                pass
            elif(len(s)==2):
                pyautogui.hotkey(s[0])
            elif(len(s)==3):
                pyautogui.hotkey(s[0],s[1])
            elif(len(s)==4):
                pyautogui.hotkey(s[0],s[1],s[2])
            elif(len(s)==5):
                pyautogui.hotkey(s[0],s[1],s[2],s[3])
            elif(len(s)==6):
                pyautogui.hotkey(s[0],s[1],s[2],s[3],s[4])
            else:
                pass
        else:
            if(i+1<len(j) and j[i]!='['and j[i]!=']'):
                pyautogui.press(j[i])
                s=''
            i+=1
