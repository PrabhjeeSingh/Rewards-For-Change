# import Utilities
# from random import randint
import fileinput
import sys


# Scanner
scan = "change"
#
#
#
#
#
name = ""  # Given
score = 15  # Given
prize = ""  # Given
people = {name: [score, prize]}
# Score Change

# Utilities.win(people, name, scan)

# # Reward
# Pressed = "Yes"
# if Pressed == "Yes":  # if button pressed
#     Utilities.reward(people, name)

f_name="qr.html"


for line in fileinput.FileInput(f_name,inplace=10):
  
  
    if "document.getElementById('x').innerHTML=" in line:
        line=line.replace(line,"document.getElementById('x').innerHTML='"+str(score)+"%';"+'\n')
        
    
    if "document.getElementById('x').style.width" in line:
        line=line.replace(line,"document.getElementById('x').style.width='"+str(score)+"%';"+'\n')



    sys.stdout.write(line)

