# def convolution_layer_1(image,filter,width,height,filter_width,filter_height):
#     for i in range(width):
#         for j in range(height):
#
#
#
#
# import urllib.request
# import ssl
# from urllib.request import urlopen
#
# from PIL import Image
# url = 'https://c.saavncdn.com/artists/Ranbir_Kapoor.jpg'
#
# im = Image.open(urllib.request.urlopen(url))
#
# im.save('/Users/manasasingh/Desktop/cnn.png')
# from PIL import Image
#
# data = im.getdata()
# width, height = im.size
#
# r = [d[0] for d in data]
# g = [d[1] for d in data]
# b = [d[2] for d in data]
#
# # Kernel/Filter, K =
# # 1  0  1
# # 0  1  0
# # 1  0  1
# filter_red=[[-1,-1,1],[0,1,-1],[0,1,1]]
# filter_green=[[1,0,0],[1,-1,-1],[1,0,-1]]
# filter_blue=[[0,1,1],[0,1,0],[1,-1,1]]
#
# filter_width=3
# filter_height=3
#
# convolution_layer_1(r,filter_red,width,height,filter_width,filter_height)
#
# layer_1_width=width-filter_width+1
# layer_1_height=height-filter_height+1
#
# im.putdata(r)
# im.save('/Users/manasasingh/Desktop/r.png')
# im.putdata(g)
# im.save('/Users/manasasingh/Desktop/g.png')
# im.putdata(b)
# im.save('/Users/manasasingh/Desktop/b.png')
#
#
