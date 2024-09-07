import cv2
import tkinter as tk
from tkinter import filedialog
def load_img():
    img_path = filedialog.askopenfilename(title="Select image file",
                                          filetypes=[("image files", "*.png;*.jpg,*.jpeg,*.gif")])
    print(img_path)
    if img_path == "":
        print("Unable to load image...")
        return
    img = cv2.imread(img_path)
    return img

def show_img(img):
    # grey_scale_img = apply_grey_scale(img)
    cropped_img = crop_img(img,0,0,200,200)
    resized_img = resize_img(img,50)
    # display image in window
    cv2.imshow("original image",img)
    # cv2.imshow("cropped image",cropped_img)
    cv2.imshow("resized image",resized_img)
    #wait until a key is pressed and then close window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def crop_img(img,x,y,width,height):
    cropped_img = img[y:y+height , x:x+width]
    return cropped_img

def resize_img(img,scale_percentage):
    width = int(img.shape[1]*scale_percentage/100)
    height = int(img.shape[0]*scale_percentage/100)

    resize_img = cv2.resize(img,(width,height))
    return resize_img

def rotate_img(img,angle):
    center = (img.shape[1] // 2 , img.shape[0] // 2)
    matrix = cv2.getRotationMatrix2D(center,angle,1.0)
    rotated_img = cv2.warpAffine(img,matrix,(img.shape[1],img.shape[0]))
    # warpAffine is used to rotate the image
    return rotated_img


def display_img(img,windowName):
    cv2.imshow(windowName, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def apply_grey_scale(img):
    # convert image to grey scale
    grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return grey_img

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    img = load_img()
    # show_img(img)
    rotated_img = rotate_img(img,130)
    display_img(rotated_img,"rotatedImg")

