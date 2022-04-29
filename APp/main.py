import tkinter as tk
import cv2
from pyzbar.pyzbar import decode

window =  tk.Tk() 


capture_qrcode = cv2.VideoCapture(0) #Captures Qr code using camera. Returns boolean, frame.
capture_qrcode.set(4, 760) #Sets Dimensions for Width (width, pixels)
capture_qrcode.set(6, 350) #Sets Dimensions for height (height, pixels)
counter=[]
score =15

cam = True

def scanner(score):
    while cam == True:
        success, frame = capture_qrcode.read() #Stores frame
        for code in decode(frame):
            if code.data.decode ('utf-8') not in counter:
                print(code.data.decode('utf-8'))
                counter.append(code.data.decode('utf-8'))
                score += 1
                return score
            elif code.data.decode('utf-8') in counter:
                pass #Exits loop. If you want to exit out of the camera/window use break, cam = false, or use cam.release() but you're going to get a small warning so keep that in mind

        cv2.imshow('Scan', frame) #Displays img
        cv2.waitKey(1) #Presents frame for 1 ms




label = tk.Label(text = "Lets get started with Scavenger hunt ;)", fg="white",
    bg="black",
    width=10,
    height=10)



window.mainloop()








