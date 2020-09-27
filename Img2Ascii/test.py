import cv2
import numpy as np

imgpath = input("Enter Path to Image: ")

#Use only if background is transparent
#
#imgpath[-3:] == "png"
#img = cv2.imread(imgpath, cv2.IMREAD_UNCHANGED) 
#print("png")
#trans_mask = img[:,:,3] == 0
#img[trans_mask] = [255, 255, 255, 255]
#img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

#Reading in image as grayscale
img = cv2.imread(imgpath,0)

#array of 64 ascii chars in order of density; scaler = 0.25
chars = ['$','@','B','%','8','&','W','M','#','*','o','a','h','k','b','d','p','q','w','m','Z','O','0','Q','L','C','J','U','Y','X','z','c','v','u','n','x','r','j','f','t','/','|','(','1','{','[','?,','-','_','+','~','<','i','!','l','I',';',':',',','\"','^','`','.',' ']

#array of 4 ascii chars in order of density; scaler = 0.015625
#chars = ['▓','▒','░',' ']

#print and get image width and height
print(img.shape)
width = img.shape[1]
height = img.shape[0]

#resolution of ascii art
res_y=int(input("Enter Y-axis resolution: "))
div = int(height/res_y)
res_x = int(width/div)

#for loop to print relevant ascii char depending on avg luminance value in a block of pixels
for i in range(res_y):
    y = div*i
    yplus = y+div
    for j in range(res_x):
        pos_top = div*j
        pos_end = pos_top+div
        Lavg = int(cv2.mean(img[y:yplus, pos_top:pos_end])[0])
        print(chars[int(Lavg*.25)], end=" ")
    print("")

cv2.waitKey(0)
