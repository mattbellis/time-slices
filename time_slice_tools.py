import numpy as np
import cv2

def take_movie(nframes = 150):

    frame_count = 0
    frames = []

    cap = cv2.VideoCapture(0)

    while(frame_count<nframes):
        # Capture frame-by-frame
        ret, frame = cap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        #webcam_preview = plt.imshow(frame)  
        
        frames.append(frame)
        frame_count += 1
        
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        

        # Display the resulting frame
        #cv2.imshow('frame',frame)
        cv2.imshow('frame',gray)
        #plt.imshow('frame')

        '''
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        '''
        
    # When everything done, release the capture# Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()

    return frames


################################################################################
def get_frame_rate():

    # Start default camera
    video = cv2.VideoCapture(0);

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    #print(major_ver, minor_ver, subminor_ver)
         
    fps = 1.0
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    dt = 1.0/float(fps)
    print("The time difference between different frames is %.3f seconds" % (dt))

    video.release()

################################################################################
def img_dist(a,b):

    mat = np.zeros((len(a),len(a[0])))

    diff = b.astype(int) - a.astype(int)

    diff *= diff
    
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            mat[i][j] = diff[i][j].sum()
    
    return mat

     
def overlay_images(frames,threshold=1500,nframes_to_skip=3):
    nframes = len(frames)

    starter_image = frames[0]

    lx = len(starter_image)
    ly = len(starter_image[0])

    newimg = starter_image.copy()

    for i in range(1,nframes,nframes_to_skip):

        img = frames[i]
        #print("---------")

        diff = img_dist(img,starter_image)
        a = diff.flatten()
        print(i,np.sort(a)[-5:])

        change_pixels = diff>threshold

        newimg[change_pixels] = img[change_pixels]


    return newimg
