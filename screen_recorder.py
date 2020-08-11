# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:57:18 2020

@author: vivek9patel (github)
"""
import cv2
import tkinter as tk
import numpy as np
import pyautogui
from tkinter.filedialog import asksaveasfilename
import time
import sys

def run():
    # display screen resolution, get it from your OS settings
    SCREEN_SIZE = pyautogui.size()
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # create the video write object
    file_name = asksaveasfilename(confirmoverwrite=False,defaultextension='.avi')
    out = cv2.VideoWriter(file_name, fourcc, 20.0, (SCREEN_SIZE))
    print("Recording Started...\n")
    odd=1
    while True:
        odd+=1
        # make a screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if(odd==10):
            cv2.imshow("Recording...", frame)
            odd=1
        # if the user clicks q, it exits
        if cv2.waitKey(1) == ord("q"):
            cv2.destroyAllWindows()
            break
        # write the frame
        out.write(frame)
    out.release()
    root.destroy()
    sys.exit(0)

def screenshot():
    root.destroy()
    print("Screen Shot...\n")
    time.sleep(1)
    myScreenshot = pyautogui.screenshot()
    file_name = asksaveasfilename(confirmoverwrite=False,defaultextension='.png')
    myScreenshot.save(file_name)
    sys.exit(0)
    
root = tk.Tk()
root.title("Screen Recorder")
root.geometry("600x220")

root.configure(background = '#e6e5e5')
frame = tk.Frame(root,bg = '#e6e5e5',pady = 1, width =550, height = 50)
frame.grid(row=0,column=0)
frame.pack()  
label0 = tk.Label(frame,font=('Comic Sans MS',26,'bold'),text = "          Screen Recorder          ",bg= '#663300',fg='white',justify ="center")
label0.pack(side=tk.TOP)
button =tk.Button(frame, font=('arial', 20,'bold'), text="Start Recording",padx=2,pady=2, bg="green",fg = "white",command=run)
button.pack(side=tk.TOP)
button1 =tk.Button(frame, font=('arial', 20,'bold'), text="Take Screenshot",padx=2,pady=2, bg="orange",fg = "white",command=screenshot)
button1.pack()
root.mainloop()
