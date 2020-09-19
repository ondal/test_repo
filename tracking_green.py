import cv2
import numpy as np


cap = cv2.VideoCapture(0)

fps = int(cap.get(cv2.CAP_PROP_FPS))
cols = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2)
rows = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/2)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, cols)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, rows)

print('fps : ', fps,',  ', cols,' x ', rows)

#
blue1 = np.array([90, 50, 50])
blue2 = np.array([120, 255,255])
green1 = np.array([45, 50,50])
green2 = np.array([75, 255,255])
red1 = np.array([0, 50,50])
red2 = np.array([15, 255,255])
red3 = np.array([165, 50,50])
red4 = np.array([180, 255,255])
yellow1 = np.array([20, 50,50])
yellow2 = np.array([35, 255,255])

tracking_lower = green1
tracking_upper = green2

#tracking_lower = blue1
#tracking_upper = blue2

#tracking_lower = yellow1
#tracking_upper = yellow2

'''
# 
mask_blue = cv2.inRange(hsv, blue1, blue2)
mask_green = cv2.inRange(hsv, green1, green2)
mask_red = cv2.inRange(hsv, red1, red2)
mask_red2 = cv2.inRange(hsv, red3, red4)
mask_yellow = cv2.inRange(hsv, yellow1, yellow2)

#
res_blue = cv2.bitwise_and(img, img, mask=mask_blue)
res_green = cv2.bitwise_and(img, img, mask=mask_green)
res_red1 = cv2.bitwise_and(img, img, mask=mask_red)
res_red2 = cv2.bitwise_and(img, img, mask=mask_red2)
res_red = cv2.bitwise_or(res_red1, res_red2)
res_yellow = cv2.bitwise_and(img, img, mask=mask_yellow)
'''
prev_x = 0

while cap.isOpened():
    
    ret, img = cap.read()
    
    #draw = img.copy()
    
    # VGR 2 HSV    
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # get the mask form target color range
    mask_color = cv2.inRange(hsv_img, tracking_lower, tracking_upper)    
    # delete the noise
    mask_color = cv2.erode(mask_color, None, iterations=2)
    # back to original size
    mask_color = cv2.dilate(mask_color, None, iterations=2)
    ret, mask_th = cv2.threshold(mask_color, 127, 255, cv2.THRESH_BINARY_INV)
          
    # get contours from the mask
    _, cnts, _ = cv2.findContours(mask_color.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cnts, _ = cv2.findContours(mask_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    center = None
    
    if len(cnts) > 0:
        #print('cnts=%d' %len(cnts), cnts)
        #print('contourArea=', cv2.contourArea)
        # get the each contour's area by cv2.contourArea and pick the largest one and return big contour
        c = max(cnts, key=cv2.contourArea)
        #print('c=', c)
        
        # get the min enclosing circle polar coordinate from the biggest contour, c 
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        
        #print('radius=', radius)
        if radius >= 10 : # detect target min size.
            # get the moment of contour, and from it, get the center 
            M = cv2.moments(c)
            center = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])
            #cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
            
            # draw the circle at center of object center
            cv2.circle(img, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(img, center, 5, (0, 0, 255), -1)
            
        if abs(prev_x-x) > 5:
            prev_x = x
            # tracking the motor.
                  
    cv2.imshow("Frame", np.hstack((img, cv2.cvtColor(mask_th, cv2.COLOR_GRAY2BGR))))
    
    #mask_inv = cv2.bitwise_not(mask_color)  
    #res_color = cv2.bitwise_and(img, img, mask=mask_color)    
    #res_color = cv2.bitwise_and(img, img, mask=mask_inv)
    # get the roi area with size, angle & etc
    # select the big one
    # overlap the img and retangle, 
    # display side by side show, draw and res_color
     
    
    '''
    roi = img2[y:h, x:w]
    fg = cv2.bitwise_and(img1, img1, mask=mask_inv)
    bg = cv2.bitwise_and(roi, roi, mask=mask)
    img2[y:h, x:w] = fg + bg
    '''
    
    #img2 = cv2.cvtColor(mask_color, cv2.COLOR_GRAY2BGR)
    
    #print(mask.shape)
    
    #cv2.imshow('Camera', img2)
    
    #cv2.imshow('Camera', res_color)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
else:
    print('Camera is not ready')

cap.release()
cv2.destroyAllWindows()

    
