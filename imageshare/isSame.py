from PIL import Image

im1=Image.open(r"C:\Users\hp\PycharmProjects\finalyear\static\images\K_Merged_Image\map.png")
im1_val=list(im1.getdata())

im2=Image.open(r"C:\Users\hp\PycharmProjects\finalyear\static\images\Input_Image\map.jpg")
im2_val=list(im2.getdata())

if im1_val==im2_val:
    print("Same")
else:
    print("Different")