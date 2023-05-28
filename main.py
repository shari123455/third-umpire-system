import tkinter
import cv2  # it used to capture vidio using Opencv to use it pip
import threading # we import this because we not need any blockage 
from functools import partial
import imutils
import time #we set time


import PIL.Image, PIL.ImageTk  # PIL mean python image library  # to install pip install pillow
# imagetk is used to show the image in the kinterwindow 
# def play(speed):
#     pass


    

root=tkinter.Tk()
stream=cv2.VideoCapture("my.mp4")  #take video in form of pixels

def play(speed):
    print(f"The speed is {speed}")
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    grabbed,frame=stream.read()
    frame=imutils.resize(frame,width=set_width,height=set_height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor= tkinter.NW)
    
  
def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("dc.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=set_width, height=set_height)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    canvas.create_text(150,30, fill ="black" , font= "times 26 bold", text= "decision by shari" )
    # 2. then wait for 1 second
    time.sleep(3)
    
    # 3. then display sponser image
    frame = cv2.cvtColor(cv2.imread("sp.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = set_width, height=set_height)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor= tkinter.NW)
    # 4. wait for 1.5 second 
    
    
    # 5. display out/notout image
    if decision== 'out':
        decisionI = "out.jpg"
    else:
        decisionI = "not out.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionI), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = set_width, height=set_height)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor= tkinter.NW)
    
    
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")
    
   
    
    
   
    
   

   
 


# This is the width and height of our main screen
set_width=650
set_height=500
root.title("i am third umpire")

cv_img = cv2.cvtColor(cv2.imread("s.jpg"), cv2.COLOR_BGR2RGB)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))

canvas = tkinter.Canvas(root,width=set_width, height=set_height) # now we set a width height and wnidow

image_on_canvas = canvas.create_image(0,0, anchor = tkinter.NW, image = photo)

canvas.pack()


btn = tkinter.Button(root, text= "<<Previous (Fast)", width=50,bg="red",command=partial(play,-25))
btn.pack()

btn = tkinter.Button(root, text="<<Previous slow", width=50 ,command=partial(play,-2))
btn.pack()

btn = tkinter.Button(root,text="Next (slow) >>", width = 50,command=partial(play,2))
btn.pack()
btn = tkinter.Button(root, text="Next (fast) >>" , width = 50,command=partial(play,25))
btn.pack()

btn = tkinter.Button(root , text = "Give out" , width=50,command=partial(out,))
btn.pack()

btn = tkinter.Button(root, text  ="Give not out" , width =50,command=partial(not_out,))
btn.pack()

btn = tkinter.Button(root, text=">> Rate Abdullah's coding `<<", width = 50,)
btn.pack()


root.mainloop()