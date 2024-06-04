from django.http import HttpResponse
from django.views import View
from imageshare.models import *
from django.shortcuts import render,redirect
from django.urls import resolve
from django.contrib.auth.mixins import LoginRequiredMixin
from imageshare.e import *
from imageshare.d import *
from imageshare.rsa import *

p,q=1,1
n=1
fn=0
e,d=0,0
class renderHomePage(View):
    def get(self,request):
        return render(
            request,
            template_name='imageshare/index.html'
        )
class renderEncryptPage(View):
    def get(self,request):
        return render(
            request,
            template_name='imageshare/encryptPage.html'
        )

    def post(self,request):
        if request.POST.get('home'):
            return render(request,template_name='imageshare/index.html')

        image_name = request.POST['pic']
        print(image_name)
        file_name=image_name
        image_name = 'C:/Users/hp/PycharmProjects/finalyear/static/images/Input_Image/'+image_name
        n_share = request.POST['n_shares']
        k_share = request.POST['k_shares']
        encrypt_key = request.POST['user_key']

        p=int(request.POST['p'])
        q=int(request.POST['q'])
        n=p*q

        fn=(p-1)*(q-1)
        e=get_e(p,q,fn)
        d = get_d(e, fn)
        email_id = request.POST['mail_ids']
        email_id_list=email_id.split("\r\n")
        file_loc="C:/Users/hp/PycharmProjects/finalyear/Reference_Files/"+file_name[:-4]+".txt"
        f=open(file_loc,'w+')
        f.write(str(p)+","+str(q)+","+str(n)+","+str(fn)+","+str(e)+","+str(d)+"\n")
        f.write("("+n_share+","+k_share+")"+","+encrypt_key)
        f.close()
        n_images=divideToNShare(image_name, n_share, k_share, encrypt_key,e,n,email_id_list)

        return render(
            request,
            template_name='imageshare/n_shares.html',
            context={'n_images': n_images,}
        )



class renderDecryptPage(View):
    def get(self,request):
        return render(
            request,
            template_name='imageshare/decryptPage.html'
        )

    def post(self,request):
        form=request.POST
        k_share = request.POST['k_value']
        decrypt_key = request.POST['decrypt_pass']
        path="C:/Users/hp/PycharmProjects/finalyear/static/images/N_Shares/"
        #d=get_d(e,fn)
        d=int(request.POST['d_value'])
        n=int(request.POST['n_value'])
        k_image=[]
        for file in request.FILES.getlist('k_image'):
            k_image.append(path+str(file))

        merged_image=mergeToKShare(k_image,k_share,d,n,decrypt_key)

        return render(
            request,
            template_name='imageshare/mergedImage.html',
            context = {'merged_image': merged_image, }
        )