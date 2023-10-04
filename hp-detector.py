from cgitb import text
import webbrowser
import imp
import time
import cv2
import mss
import numpy
import pytesseract
import os
from playsound import playsound

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    
previous_hp = None

with mss.mss() as sct:
    while "Screen capturing":
        monitor = {"top": 1000, "left": 575, "width": 70, "height": 50}
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        cong = r'--oem 3 --psm 6 outputbase digits'

        text = pytesseract.image_to_string(img, config=cong)
        
        current_hp = [text]

        # Check if max_hp has changed
        if previous_hp is not None and previous_hp != current_hp:
            print("Max HP has changed from", previous_hp, "to", current_hp)

        if current_hp == ["100\n"]:
            print("you currently have max hp", current_hp)
        else:
            if previous_hp != current_hp:
                playsound("C:/Users/Kasutaja/Desktop/Valo stuff/theSound.mp3") # here you can basically add any punishment you want, for me it just plays a loud sound.
                print("You have taken damage, your new health is: ", current_hp)
            max_hp = current_hp

        # Set previous_hp to the current value
        previous_hp = current_hp
       
        # Display the picture in grayscale
        cv2.imshow('OpenCV/Numpy grayscale',
        cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break