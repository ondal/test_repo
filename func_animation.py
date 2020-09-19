import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class video:
        
    def __init__(self, device=0):
        
        self.cap = cv2.VideoCapture(device)
        self.retval, self.frame = self.cap.read()
        
        self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)) 
        print('start capture...')
                
        
    def updateFrame(self, k):
        self.retval, self.frame = self.cap.read()
        #print('update...')
        self.im.set_array(cv2.cvtColor(camera.frame, cv2.COLOR_BGR2RGB))
                
    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print('finish capture')

    
class Video(animation.FuncAnimation):
        
    def __init__(self, device=0, fig = None, frames = None,
                 interval = 50, repeat_delay = 5, blit = False, **kwargs):
        
        if fig is None:
            self.fig = plt.figure()
            self.fig.canvas.set_window_title('Video Capture')
            plt.axis('off')
            
        super(Video, self).__init__(self.fig, self.updateFrame, init_func = self.init, 
                                    frames = frames, interval = interval, blit =blit,
                                    repeat_delay = repeat_delay, **kwargs)
        self.cap = cv2.VideoCapture(device)
        self.retval, self.frame = self.cap.read()
        
        self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)) 
        print('start capture...')
                
    def init(self):
        retval, self.frame = self.cap.read()
        if retval:
            self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)) 
        
    def updateFrame(self, k):
        retval, self.frame = self.cap.read()
        if retval:
            self.im.set_array(cv2.cvtColor(camera.frame, cv2.COLOR_BGR2RGB))
                
    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print('finish capture')

class Video2(animation.FuncAnimation):
        
    def __init__(self, device=0, fig = None, frames = None,
                 interval = 80, repeat_delay = 5, blit = False, **kwargs):
        
        if fig is None:
            self.fig, self.ax = plt.subplots(1, 2, figsize = (10,5))            
            self.fig.canvas.set_window_title('Video Capture')
            self.ax[0].set_position([0, 0, 0.5, 1])            
            self.ax[0].axis('off')
            self.ax[1].set_position([0.5, 0, 0.5, 1])            
            self.ax[1].axis('off')            
            
        super(Video2, self).__init__(self.fig, self.updateFrame, init_func = self.init, 
                                    frames = frames, interval = interval, blit = blit,
                                    repeat_delay = repeat_delay, **kwargs)
        
        self.cap = cv2.VideoCapture(device)
        print('start capture...')
                
    def init(self):
        retval, self.frame = self.cap.read()
        if retval:
            self.im0 = self.ax[0].imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB), aspect='auto') 
            self.im1 = self.ax[1].imshow(np.zeros(self.frame.shape, self.frame.dtype), aspect='auto')
            
    def updateFrame(self, k):
        #print('update...')
        retval, self.frame = self.cap.read()
        if retval:
            self.im0.set_array(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
            
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            self.im1.set_array(cv2.merge((gray,gray,gray)))
                
    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print('finish capture')


if True:
    camera = Video2()
    plt.show()
    camera.close()
    
elif False:   
    camera = Video()
    plt.show()
    camera.close()
    
elif False:
    fig = plt.figure()
    fig.canvas.set_window_title('Video Capture')
    plt.axis('off')
    
    camera = video()
    ani = animation.FuncAnimation(fig, camera.updateFrame, interval = 50)
    plt.show()
    camera.close()
    
elif True:
    cap = cv2.VideoCapture(0)
    fig = plt.figure(figsize =(10, 6))
    fig.canvas.set_window_title('Video Capture')
    plt.axis('off')
    
        
    def init():
        global im
        retval, frame = cap.read()
        
        im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        
    def updateFrame(k):
        global im
        
        retval, frame = cap.read()
        
        if retval:
            im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
    ani = animation.FuncAnimation(fig, updateFrame, init_func = init, interval = 50)
    plt.show()
    
    if cap.isOpened():
        cap.release()        
    
