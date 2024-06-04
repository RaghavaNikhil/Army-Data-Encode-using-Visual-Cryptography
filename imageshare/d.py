from PIL import Image
from imageshare.ceaser import *
from imageshare.rsa import *
import csv

def mergeToKShare(k_image,k_share,d,n,decrypt_key):
    k=int(k_share)
    kth=1
    width=0
    height=0
    total_len=0
    result=[]
    index=0
    while kth<=k:

        kth_image_name=k_image[index]
        index+=1

        if kth==1:
            im = Image.open(kth_image_name)
            result = list(im.getdata())
            width, height = im.size
            total_len=width*height
            for i in range(total_len):
                result[i]=list(result[i])
        else:
            im=Image.open(kth_image_name)
            kth_image=list(im.getdata())
            for i in range(total_len):
                r = kth_image[i][0]
                g = kth_image[i][1]
                b = kth_image[i][2]
                result[i][0] = result[i][0] or r
                result[i][1] = result[i][1] or g
                result[i][2] = result[i][2] or b

        kth+=1

    dec_img = Image.new("RGB", (width, height))
    #storing result if received images is less than k
    result_temp=result

    for i in range(len(result)):
        result[i]=tuple(result[i])
    save_merged_int_image_as = "merged_int_" + k_image[0].split("/")[-1][0:-5]+k_image[0].split("/")[-1][-4:]
    path_save_merged_int_image = "C:/Users/hp/PycharmProjects/finalyear/static/images/Intermediate_Merged_Image/" + save_merged_int_image_as
    dec_img.putdata(result)
    dec_img.save(path_save_merged_int_image)

    im1=Image.open(path_save_merged_int_image)
    im2=Image.open(r"C:/Users/hp/PycharmProjects/finalyear/static/images/Encrypted_Images/"+"encrypted_"+k_image[0].split("/")[-1][0:-5]+".png")

    result=[]
    csv_file = "C:/Users/hp/PycharmProjects/finalyear/CSV_files/" + k_image[0].split("/")[-1][0:-5]+".csv"
    if(im1==im2):
        with open(csv_file, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                result.append(list(map(int, row[0].split(','))))
    else:
        result = result_temp

    im = Image.new("RGB", (width, height))
    pix = im.load()
    index=0
    #RSA Decryption
    result=rsa_decryption(result,d,n)

    #using ceaser cipher
    result=decryptImage(result,decrypt_key)
    for j in range(height):
        for k in range(width):
            r=result[index][0]
            g=result[index][1]
            b=result[index][2]
            index+=1
            pix[k, j] = (r,g,b)

    path="C:/Users/hp/PycharmProjects/finalyear/static/images/K_Merged_Image/"
    merged_image_name=path+k_image[0].split("/")[-1][0:-5]+".png"
    im.save(merged_image_name)

    return merged_image_name


