
import cv2
import os
import easygui

#to open the file dialog box
path = easygui.fileopenbox()

cam = cv2.VideoCapture(path)
  
try:
    #if data folder not found creates new folder
    if not os.path.exists('data'):
        os.makedirs('data')
  
except OSError:
    print ('Error: Creating directory of data')
  

currentframe = 0
  
while(True):
    #ret return a boolean that is whether the frame is available or not & frame return the frame  
    ret,frame = cam.read()
    
    #if ret is true then we would save the obtained frame to the data folder made
    if ret:
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        #cv2.imwrite writes the frames to the folder
        cv2.imwrite(name, frame)
  
        
        currentframe += 1
    else:
        #at the end of the video the frames are not available then the ret returns false and the while loop is exited
        break
  

cam.release()
cv2.destroyAllWindows()