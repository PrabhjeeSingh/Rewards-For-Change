import cv2 #Identifies Qr code
from pyzbar.pyzbar import decode
import fileinput
import sys

score = 15
# Scanner
capture_qrcode = cv2.VideoCapture(0) #Captures Qr code using camera. Returns boolean, frame.
capture_qrcode.set(4, 760) #Sets Dimensions for Width (width, pixels)
capture_qrcode.set(6, 350) #Sets Dimensions for height (height, pixels)
counter = []

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
var1 = scanner(score)
scan = "change"
print(var1)



people = {name: [score, prize]}
# Score Change

# Utilities.win(people, name, scan)

# # Reward
# Pressed = "Yes"
# if Pressed == "Yes":  # if button pressed
#     Utilities.reward(people, name)

f_name = "qr.html"

for line in fileinput.FileInput(f_name, inplace=10):

    if "document.getElementById('x').innerHTML=" in line:
        line = line.replace(line, "document.getElementById('x').innerHTML='" + str(var1) + "%';" + '\n')

    if "document.getElementById('x').style.width" in line:
        line = line.replace(line, "document.getElementById('x').style.width='" + str(var1) + "%';" + '\n')

    sys.stdout.write(line)

