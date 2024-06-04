from PIL import Image
import random
from imageshare.ceaser import *
from imageshare.SendMail import  *
from imageshare.rsa import *
import csv

def divideToNShare(image_name,no,k_share,encrypt_key,e,n,email_id_list):
    no=int(no)
    k_share=int(k_share)
    total_email_ids=len(email_id_list)
    recons=(no-k_share)+1
    save_enc_image_as="encrypted_"+image_name.split("/")[-1][0:-4]
    path_save_enc_image="C:/Users/hp/PycharmProjects/finalyear/static/images/Encrypted_Images/"+save_enc_image_as+".png"
    im = Image.open(image_name)

    pix_val = list(im.getdata())

    width, height = im.size
    total_pix=width*height
    pix_val_tup=[]
    for i in range(total_pix):
        pix_val[i]=list(pix_val[i])

    #Ceaser Ciper Encryption
    pix_val=encryptImage(pix_val, encrypt_key)
    #RSA Encryption
    pix_val=rsa_encryption(pix_val,e,n)
    for i in range(total_pix):
        pix_val[i]=tuple(pix_val[i])

    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(pix_val)
    encrypted_img.save(path_save_enc_image)

    f=open("Temp.txt","w+")
    f.write(str(pix_val))

    csv_file = "C:/Users/hp/PycharmProjects/finalyear/CSV_files/" + image_name.split("/")[-1][0:-4]+".csv"
    with open(csv_file, 'w', newline='') as out:
        csv_out = csv.writer(out)
        for i in pix_val:
            csv_out.writerow(i)


    n_share = [[[0,0,0] for col in range(total_pix)] for row in range(no)]
    for i in range(total_pix):
        a = list(range(no))
        size = no
        for h in range(recons):
            r = random.choice(a)
            ind = a.index(r)
            a[ind] = a[size - 1]
            a = a[:-1]
            size -= 1
            n_share[r][i]=pix_val[i]

    email_id_index=0
    email_id_index_temp=0
    iname=(image_name.split("/")[-1]).split(".")[0]
    n_images=[]
    mailer = Email_Sender()

    for i in range(no):
        im = Image.new("RGB", (width, height))
        pix = im.load()
        name=iname+str(i+1)+".png"
        index=0
        for j in range(height):
            for k in range(width):
                r = n_share[i][index][0]
                g = n_share[i][index][1]
                b = n_share[i][index][2]

                pix[k,j] = (r,g,b)
                index+=1
        im_name="C:/Users/hp/PycharmProjects/finalyear/static/images/N_Shares/"+name
        im.save(im_name)
        im_name="images/N_Shares/"+name

        if email_id_index_temp<total_email_ids:
            n_images.append((im_name,email_id_list[email_id_index_temp]))
            email_id_index_temp+=1
        else:
            n_images.append((im_name,"No Email Given"))

        if email_id_index < total_email_ids:
            mailer.send_email(email_id_list[email_id_index], "/Users/hp/PycharmProjects/finalyear/static/"+im_name)
            email_id_index+=1
    return n_images
