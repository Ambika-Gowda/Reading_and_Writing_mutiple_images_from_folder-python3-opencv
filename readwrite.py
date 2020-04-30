import cv2
import glob
import os


def readWriteMutipleImages():
    
    d = 0
    # Folder containing the all the images folder
    dir_path = "/home/ambi/Documents/readimages/"
    # Get all the images ending with jpg
    files = glob.glob(os.path.join(dir_path,"*.jpg"))
    # Iterate through files and get one image at a time
    for img in files:
        # Read one image at a time
        frame = cv2.imread(img)

        # Path to write the image to folder
        path = "/home/ambi/Documents/writeimages/image_%d.jpg"%d
        # Will write image with specified path
        cv2.imwrite(path,frame)
        # Increment the counter for writing image name
        d+=1

        # Display the image
        cv2.imshow('Display_image', frame)
        #wait for 1 second
        k = cv2.waitKey(1000)
        #destroy the window
        cv2.destroyAllWindows()


if __name__ == '__main__':

    readWriteMutipleImages();