import cv2

def output(in_file,out_file,func):
    print("Start to processing "+in_file)
    image = cv2.imread(in_file)
    a1 = func(image)
    cv2.imwrite(out_file,a1)
    print("FInished image processing!")

def outputAll(in_file,out_file,func_array):
    print("Start to processing "+in_file)
    image = cv2.imread(in_file)
    for i in range(len(func_array)):
        print("Iteration "+str(i))
        if i==0:
            a1 = func_array[i](image)
        else:
            a1 = func_array[i](a1)
    cv2.imwrite(out_file,a1)
    print("FInished image processing!")