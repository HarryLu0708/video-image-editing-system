import cv2
import dlib

def addChristmasHat(img):
    hat_img = cv2.imread("materials/christmashat_r.png",cv2.IMREAD_UNCHANGED)
    r,g,b,a = cv2.split(hat_img)
    rgb_hat = cv2.merge((r,g,b))
    cv2.imwrite("materials/alpha_hat.jpg",a)

    path = "shape_predictor_5_face_landmarks.dat"
    predictor = dlib.shape_predictor(path)

    detector = dlib.get_frontal_face_detector()

    dets = detector(img,1)

    if len(dets)>0:
        for d in dets:
            x,y,w,h = d.left(),d.top(),d.right()-d.left(),d.bottom()-d.top()
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2,8,0)
            shape = predictor(img,d)
            for point in shape.parts():
                cv2.circle(img,(point.x,point.y),3,color=(0,255,0))
            cv2.imwrite("out_files/images/det.jpg",img)
            point1 = shape.part(0)
            point2 = shape.part(2)
            eye_center = ((point1.x+point2.x)//2,(point1.y+point2.y)//2)
            factor = 1.5
            resize_hat_h = int(round(rgb_hat.shape[0]*w/rgb_hat.shape[1]*factor))
            resize_hat_w = int(round(rgb_hat.shape[1]*w/rgb_hat.shape[1]*factor))
            if resize_hat_h>y:
                resize_hat_h = y
            resized_hat = cv2.resize(rgb_hat,(resize_hat_w,resize_hat_h))
            mask = cv2.resize(a,(resize_hat_w,resize_hat_h))
            mask_inv = cv2.bitwise_not(mask)
            dh = 0
            dw = 0
            bg_roi = img[y+dh-resize_hat_h:y+dh,(eye_center[0]-resize_hat_w//3):(eye_center[0]+resize_hat_w//3*2)]
            bg_roi = bg_roi.astype(float)
            mask_inv = cv2.merge((mask_inv,mask_inv,mask_inv))
            alpha = mask_inv.astype(float)/255
            alpha = cv2.resize(alpha,(bg_roi.shape[1],bg_roi.shape[0]))
            bg = cv2.multiply(alpha,bg_roi)
            bg = bg.astype('uint8')
            cv2.imwrite('out_files/images/bg.png',bg)
            hat = cv2.bitwise_and(resized_hat,resized_hat,mask=mask)
            cv2.imwrite("out_files/images/hat.jpg",hat)

            hat = cv2.resize(hat,(bg_roi.shape[1],bg_roi.shape[0]))
            add_hat = cv2.add(bg,hat)
            img[y+dh-resize_hat_h:y+dh,(eye_center[0]-resize_hat_w//3):(eye_center[0]+resize_hat_w//3*2)] = add_hat
            #cv2.imwrite("out_files/images/hatplus.jpg",img)
            #print("FInished image processing!")
            return img






def detect(img,model="shape_predictor_5_face_landmarks.dat"):
    path = model
    predictor = dlib.shape_predictor(path)

    detector = dlib.get_frontal_face_detector()

    dets = detector(img,1)

    if len(dets)>0:
        #print("Start to recognize...")
        for d in dets:
            x,y,w,h = d.left(),d.top(),d.right()-d.left(),d.bottom()-d.top()
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2,8,0)
            shape = predictor(img,d)
            for point in shape.parts():
                cv2.circle(img,(point.x,point.y),3,color=(0,255,0))
            return img
   # print("FInished image processing!")
