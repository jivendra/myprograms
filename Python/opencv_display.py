import cv2 as cv
from cv2 import imread
img = imread('/home/jivendra/Pictures/Screenshot_20220522_140111.png')
cv.imshow('Shoe', img);
cv.waitKey(0)