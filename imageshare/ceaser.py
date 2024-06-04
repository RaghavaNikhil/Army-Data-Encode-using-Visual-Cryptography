def encryptImage(result,key):
    k=0
    for i in  key:
        k+=ord(i)
    l=len(result)
    for i in range(l):
        for j in range(3):
            result[i][j]=(result[i][j]+k)%256
    return result

def decryptImage(result,key):
    k=0
    for i in key:
        k+=ord(i)
    l=len(result)
    for i in range(l):
        for j in range(3):
            result[i][j]=(result[i][j]-k)%256
    return result

# def encryptImage(result,key):
#
#
#     inputimagebits=""
#     l=len(result)
#     for i in range(l):
#         r=str(bin(result[i][0])[2:]).zfill(8)
#         g=str(bin(result[i][1])[2:]).zfill(8)
#         b=str(bin(result[i][2])[2:]).zfill(8)
#         inputimagebits+=(r+g+b)
#
#     key_in_bits=""
#     for c in key:
#         ascii_c=ord(c)
#         c_bits=str(bin(ascii_c)[2:])
#         key_in_bits+=c_bits
#
#     no_of_times=len(inputimagebits)//len(key_in_bits)
#     rem=len(inputimagebits)%len(key_in_bits)
#
#     final_key=key_in_bits*no_of_times
#     final_key+=key_in_bits[:rem]
#
#     encrypted=""
#     for i in range(len(final_key)):
#         if inputimagebits[i]==final_key[i]:
#             encrypted+='0'
#         else:
#             encrypted+='1'
#
#     split_encrytped=encrypted
#     encrypted_img_list=[]
#     while(len(split_encrytped)!=0):
#         r=(int(split_encrytped[:8],2))
#         split_encrytped=split_encrytped[8:]
#         g = (int(split_encrytped[:8], 2))
#         split_encrytped = split_encrytped[8:]
#         b = (int(split_encrytped[:8], 2))
#         split_encrytped = split_encrytped[8:]
#         encrypted_img_list.append([r,g,b])
#
#
#     return encrypted_img_list
#
#
# def decryptImage(result, key):
#     print("mg ")
#     inputimagebits = ""
#     l = len(result)
#     for i in range(l):
#         r = str(bin(result[i][0])[2:]).zfill(8)
#         g = str(bin(result[i][1])[2:]).zfill(8)
#         b = str(bin(result[i][2])[2:]).zfill(8)
#         inputimagebits += (r + g + b)
#
#     key_in_bits = ""
#     for c in key:
#         ascii_c = ord(c)
#         c_bits = str(bin(ascii_c)[2:])
#         key_in_bits += c_bits
#
#     no_of_times = len(inputimagebits) // len(key_in_bits)
#     rem = len(inputimagebits) % len(key_in_bits)
#
#     final_key = key_in_bits * no_of_times
#     final_key += key_in_bits[:rem]
#
#     encrypted = ""
#     for i in range(len(final_key)):
#         if inputimagebits[i] == final_key[i]:
#             encrypted += '0'
#         else:
#             encrypted += '1'
#
#     split_encrytped = encrypted
#     encrypted_img_list = []
#     while (len(split_encrytped) != 0):
#         r = (int(split_encrytped[:8], 2))
#         split_encrytped = split_encrytped[8:]
#         g = (int(split_encrytped[:8], 2))
#         split_encrytped = split_encrytped[8:]
#         b = (int(split_encrytped[:8], 2))
#         split_encrytped = split_encrytped[8:]
#         encrypted_img_list.append([r, g, b])
#
#     return encrypted_img_list