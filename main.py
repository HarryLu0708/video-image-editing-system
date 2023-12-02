import filters as f
from outputs import output, outputAll
from videoprocessing import videoOut, videoAllOut
from camera_controls import cameraOn, cameraOnAll, cameraMultiOn
from detections import detect, addChristmasHat


#output('test_files/test.JPG','out_files/images/christmas.jpg',addChristmasHat)


#cameraMultiOn(f.summer,f.sepia,f.winter,f.bright,f.HDR,f.greyscale)

#cameraOn(f.winter,'f1')

#videoOut(addChristmasHat,path='test_files/test_video2.MP4',out='out_files/videos/christmas.mp4')

#func_array = [sharpen,bright,sepia]
#outputAll('test_files/test.JPG','out_files/all.jpg',func_array)
output('test_files/test.JPG','out_files/sketch.jpg',f.sketch)
#output('test_files/test.JPG','out_files/canny.jpg',f.canny)

#funcs = [f.sharpen,f.bright]
#cameraOnAll(funcs,'f2')
#cameraOn(addChristmasHat,'f3')
#videoAllOut(funcs,out="out_files/videos/all.mp4")
#outputAll('test_files/test.JPG','out_files/images/combined.jpg',funcs)




