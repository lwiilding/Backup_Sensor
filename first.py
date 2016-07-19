from Tkinter import *
from PIL import ImageTk,Image
import tkFont
import RPi.GPIO as GPIO
import smbus
import time

bus = smbus.SMBus(1)
address = 0x04

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.LOW)
x_coordinate = 280
y_coordinate = 200
win=Tk()
win.attributes("-fullscreen",True)
w = Canvas(win, width = 800, height = 480)
myFont=tkFont.Font(family='Helvetica',size=36,weight='bold')

#def ledON()://
 #   print("LED button pressed")
  #  if GPIO.input(40):
   #     GPIO.output(40,GPIO.LOW)
    #    ledButton["text"]="LED ON"
 #   else:
  #      GPIO.output(40,GPIO.HIGH)
   # ledButton["text"]="LED OFF"

#def exitProgram():
 #   print("Exit Button pressed")
  #  GPIO.cleanup()
   # win.quit()

win.title("First GUI")
win.geometry('800x480')


#exitButton = Button(win,text = "Exit",font=myFont,command=exitProgram,height=2,width=6)
#exitButton.pack(side=BOTTOM)


#ledButton = Button(win,text ="LED ON",font=myFont,command=ledON,height=2,width=8)
#ledButton.pack()
#photo = PhotoImage(file="/home/pi/Downloads/outline")

w.pack()
photo = PhotoImage(file="/home/pi/Downloads/outline")
w.create_image((x_coordinate, y_coordinate), image=photo)
rect1 = w.create_rectangle(560, 165, 566, 240, fill="green", outline='')
rect2 = w.create_rectangle(567, 160, 573, 245, fill="green", outline='')
rect3 = w.create_rectangle(574, 155, 580, 250, fill="green", outline='')
rect4 = w.create_rectangle(581, 150, 587, 255, fill="green", outline='')
rect5 = w.create_rectangle(588, 145, 594, 260, fill="green", outline='')
rect6 = w.create_rectangle(595, 140, 601, 265, fill="green", outline='')
rect7 = w.create_rectangle(602, 135, 608, 270, fill="green", outline='')
rect8 = w.create_rectangle(609, 130, 615, 275, fill="green", outline='')
rect9 = w.create_rectangle(616, 125, 622, 280, fill="green", outline='')
rect10 = w.create_rectangle(623, 120, 629, 285, fill="green", outline='')
rect11 = w.create_rectangle(630, 115, 636, 290, fill="green", outline='')
rect12 = w.create_rectangle(637, 110, 643, 295, fill="green", outline='')
        
while True:
        distance = bus.read_byte(address)
        print "Arduino: Hey RPI, an object is ", distance, " cm away."
        color="green"
        if distance < 10:
            w.itemconfig(rect1, fill="red")
        else:
            w.itemconfig(rect1, fill="green")
        if distance < 20:
            w.itemconfig(rect2, fill="red")
        else:
            w.itemconfig(rect2, fill="green")
        if distance < 30:
            w.itemconfig(rect3, fill="red")
        else:
            w.itemconfig(rect3, fill="green")
        if distance < 40:
            w.itemconfig(rect4, fill="red")
        else:
            w.itemconfig(rect4, fill="green")
        if distance < 50:
            w.itemconfig(rect5, fill="red")
        else:
            w.itemconfig(rect5, fill="green")
        if distance < 60:
            w.itemconfig(rect6, fill="red")
        else:
            w.itemconfig(rect6, fill="green")
        if distance < 70:
            w.itemconfig(rect7, fill="red")
        else:
            w.itemconfig(rect7, fill="green")
        if distance < 80:
            w.itemconfig(rect8, fill="red")
        else:
            w.itemconfig(rect8, fill="green")
        if distance < 90:
            w.itemconfig(rect9, fill="red")
        else:
            w.itemconfig(rect9, fill="green")
        if distance < 100:
            w.itemconfig(rect10, fill="red")
        else:
            w.itemconfig(rect10, fill="green")
        if distance < 110:
            w.itemconfig(rect11, fill="red")
        else:
            w.itemconfig(rect11, fill="green")
        if distance < 120:
            w.itemconfig(rect12, fill="red")
        else:
            w.itemconfig(rect12, fill="green")
        win.update()
        time.sleep(.1)
#label = Label(win,image=photo)                   
#label.pack()

#image = Image.open('/home/pi/Downloads/outline.png')
#image.show()
#win.mainloop()
