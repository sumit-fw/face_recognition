'''
Created on Jan 30, 2019

@author: Sumit
'''
import cv2
from _elementtree import Element

class camera(Element):
    def __init__(self, cameraID):
        self.camera=cameraID

    def load_Camera(self):
        '''
        initiate camera 
        :param cameraID: connection of camera default is 0 
        '''
        cam = cv2.VideoCapture(self.camera)
        return cam
    
    def realease_Camera(self):
        '''
        realease camera 
        :param cam: Camera object 
        '''
        self.camera.release()
    



class image(Element):
    def __init__(self, image):
        self.image = image

    
    def load_image_Camera(self, cam):
        '''
        Read image from camera image from camera and return object 
        :param cam: connection of camera default is 0 
        '''
        _, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return gray
    
    
    
    def load_image_file(self, file, mode='RGB'):
        '''
        Loads an image file (.jpg, .png, etc) into a numpy array
        :param file: image file name or file object to load
        :param mode: format to convert the image to. Only 'RGB' (8-bit RGB, 3 channels) and 'L' (black and white) are supported.
        :return: image contents as numpy array
        '''
        img = cv2.imread(file)
        return img
    
    
    def show_image_file(self, img,title='Window'):
        '''
        Show an image file
        :param title: Window name
        :param img: img object
        :return: NA
        '''
        img = cv2.imshow(title,img)
        
    
def face_Detection(gray):
    face_cascade = cv2.CascadeClassifier('.//face_recognition//haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.55, minNeighbors=5, minSize=(40,40))
    #for (x,y,w,h) in faces:
    #    cv2.rectangle(cam,(x,y),(x+w,y+h),(255,0,0),2)
    #    roi_gray = gray[y:y+h, x:x+w]
    #    roi_color = cam[y:y+h, x:x+w]
    return faces