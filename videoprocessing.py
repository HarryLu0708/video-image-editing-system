import cv2

def videoOut(func,path = 'test_files/test_video.MP4',out='out_files/videos/test.mp4'):
    print("Start Procesing...",path)
    vid = cv2.VideoCapture(path)
    if vid.isOpened()==False:
        print('Loading Video Failed')
    else:
        fps = int(vid.get(5))
        print("Frame Rate:",fps)
        #fps = float(vid.get(7))
        #print("Frame Rate:",fps)
        width = vid.get(3) # float `width`
        height = vid.get(4)
        print(width,',',height)
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        writer = cv2.VideoWriter(out,fourcc,fps,(1080,1920),True)
        while True:
            ret,img=vid.read()
            if not ret:
                break
            img_out = func(img)
            writer.write(img_out)
    writer.release()
    print("Finished processing...",path)

def videoAllOut(funcs,path = 'test_files/test_video.MP4',out='out_files/videos/test.mp4'):
    print("Start Procesing...",path)
    vid = cv2.VideoCapture(path)

    if vid.isOpened()==False:
        print('Loading Video Failed')
    else:
        fps = int(vid.get(5))
        print("Frame Rate:",fps)
        #fps = float(vid.get(7))
        #print("Frame Rate:",fps)
        width = vid.get(3) # float `width`
        height = vid.get(4)
        print(width,',',height)
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        writer = cv2.VideoWriter(out,fourcc,fps,(1080,1920),True)
        while True:
            ret,img=vid.read()
            if not ret:
                break
            for i in range(len(funcs)):
                if i==0:
                    img_out = funcs[i](img)
                else:
                    img_out = funcs[i](img_out)
            writer.write(img_out)
    writer.release()
    print("Finished processing...",path)


