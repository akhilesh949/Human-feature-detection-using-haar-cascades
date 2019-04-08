# Human features detection using haar cascades

A Haar Cascade is a classifier which is used to detect the object for which it has been trained for, from the source. The Haar Cascade is trained by superimposing the positive image over a set of negative images. This code makes use of the pre trained default face and eye cascade xml files to detect faces. 

## Dependencies
Python 3.0


OpenCV 
```
conda install -c menpo opencv
```
The code will work on any python IDE.
To take input frames from the primary webcam instead of a video stream, just pass 0 as the argument in 
cap = cv2.VideoCapture(0)
in place of 
cap = cv2.VideoCapture('friends.mkv')
