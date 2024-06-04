def enc(m,e,n):
    return pow(m,e,n)

def dec(c,d,n):
    return pow(c, d, n)

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

    return 0

def inverse_mod(a,b):
    for i in range(1,b):
        if a*i%b==1:
            return i
    return 0

# def power(x,y,p):
#     res=1
#     x=x%p
#     while(y>0):
#         if(y&1):
#             res=(res*x)%p
#         y=y>>1
#         x=(x*x)%p
#
#     return res


def get_e(p,q,fn):
    e=1
    for i in range(2,fn):
        if(gcd(fn,i)==1 and (i!=p and i!=q)):
            e=i
            return e

def get_d(e,fn):
    d=inverse_mod(e,fn)
    return d

#print("e=",e,"d=",d)

def rsa_encryption(new_list,e,n):
    print("Encryption........")
    enc_list=[]
    for i in range(len(new_list)):
        r = enc(new_list[i][0], e, n)
        g = enc(new_list[i][1], e, n)
        b = enc(new_list[i][2], e, n)
        enc_list.append((r,g,b))

    # encrypted_img=Image.new("RGB",(w,h))
    # encrypted_img.putdata(enc_list)
    # encrypted_img.save("rsa_enc.png")
    print("Encryption done.....")
    return enc_list

def rsa_decryption(enc_list,d,n):
    print("Decryption.......")
    dec_list=[]
    for i in range(len(enc_list)):
            r=dec(enc_list[i][0], d, n)%n
            g=dec(enc_list[i][1], d, n)%n
            b=dec(enc_list[i][2], d, n)%n
            dec_list.append([r,g,b])

    # decrypted_img=Image.new("RGB",(w,h))
    # decrypted_img.putdata(dec_list)
    # decrypted_img.save( "rsa_dec.png" )
    print("Decryption Done.....")
    return dec_list


