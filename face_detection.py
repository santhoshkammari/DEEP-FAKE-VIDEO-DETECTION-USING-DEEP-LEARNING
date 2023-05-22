# -*- coding: utf-8 -*-
"""face-detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BN6SMXGZRDqDEBJ-CG75JY27AbiQkQGD
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np

image_path="/content/download (2).jpg";
plt.imshow(mpimg.imread(image_path))

def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

haar_cascade_face = cv2.CascadeClassifier("/content/drive/MyDrive/IIITM/BTP/modelfiles/haarcascade_frontalface_default.xml")

def detect_faces(cascade, test_image, scaleFactor = 1.10):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()
    
    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    
    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image,scaleFactor,minNeighbors=7)
    
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 15)
        
    return faces_rect,image_copy

test_image = cv2.imread("/content/drive/MyDrive/IIITM/BTP/data/frame0.jpg")

# Converting to grayscale as opencv expects detector takes in input gray scale images
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Displaying grayscale image

test_image = cv2.imread("/content/download (2).jpg")
plt.imshow(convertToRGB(test_image))

!pip install face-recognition

import face_recognition

faces=face_recognition.load_image_file("/content/depositphotos_74324459-stock-photo-two-twin-babies-girls.jpg")
f_loc=face_recognition.face_locations(faces)
print(len(f_loc))

test_image2 = cv2.imread("/content/download (2).jpg")
#test_image2 = cv2.imread(image_path)
#call the function to detect faces
faces = detect_faces(haar_cascade_face, test_image2)
print ("Number of faces detected: " + str(faces[0].shape[0]))#convert to RGB and display image
plt.imshow(convertToRGB(faces[1]))

startstring="/content/drive/MyDrive/IIITM/BTP/data/frame"
endingstring=".jpg"
count_faces=0
for i in range(20): 
  img=startstring+str(i)+endingstring
  print(img)
  if detect_faces(haar_cascade_face,cv2.imread(img))[0].shape[0]>=1:
    count_faces+=1
print(count_faces)

!pip install face-recognition

!ls

import face_recognition

given_image = face_recognition.load_image_file("/content/drive/MyDrive/IIITM/BTP/data/frame0.jpg")

face_locations = face_recognition.face_locations(given_image)

number_of_faces = len(face_locations)
print("We found {} face(s) in this image.".format(number_of_faces))