import cv2
import filters as f

def cameraOn(func,frame_name='frame'):
    vid = cv2.VideoCapture(0)
    print("Camera ON...")
    while(True):
        ret,frame = vid.read()
        frame = func(frame)
        cv2.imshow(frame_name,frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    vid.release() 
    cv2.destroyAllWindows() 
    print("Camera OFF.")


def cameraOnAll(funcs,frame_name='frame'):
    vid = cv2.VideoCapture(0)
    print("Camera ON...")
    while(True):
        ret,frame = vid.read()
        for i in range(len(funcs)):
            frame = funcs[i](frame)
        cv2.imshow(frame_name,frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    vid.release() 
    cv2.destroyAllWindows() 
    print("Camera OFF.")


def cameraMultiOn(func1,func2,func3,func4,func5,func6):
    vid = cv2.VideoCapture(0)
    print("Camera ON...")
    while(True):
        ret,frame = vid.read()
        frame1 = func1(frame)
        frame2 = func2(frame)
        frame3 = func3(frame)
        frame4 = func4(frame)
        frame5 = func5(frame)
        frame6 = func6(frame)
        cv2.imshow('frame',frame1)
        cv2.imshow('frame2',frame2)
        cv2.imshow('frame3',frame3)
        cv2.imshow('frame4',frame4)
        cv2.imshow('frame5',frame5)
        cv2.imshow('frame6',frame6)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    vid.release() 
    cv2.destroyAllWindows() 
    print("Camera OFF.")

