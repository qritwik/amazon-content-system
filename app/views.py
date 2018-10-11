from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from lxml import html
import csv,os,json
import requests
import pandas as pd
from . import forms
from .models import *
from bs4 import BeautifulSoup
import http.client
import json
import ast
from django.db.models import F
from django.db.models import Q

h=[]
p=[]


def message(request):
    return render(request,'message.html')


def fetch_asin(request):
    data1 = asinDetail.objects.all()
    total_asin = data1.count()

    data2 = asinDetail.objects.filter(extracted=True)
    fetch_asin = data2.count()

    form1 = forms.form_oldDetailAmazon()

    if request.method == 'POST':
        if asinDetail.objects.filter(extracted=False).exists():
            data3 = asinDetail.objects.filter(extracted=False)
            for i in data3:
                form1 = forms.form_oldDetailAmazon(request.POST)
                sendme = asinDetail.objects.get(asin=i)
                i = i.asin
                url = "http://www.amazon.in/dp/"+i
                data4 = parse(url)
                try:
                    data4['asin']=i

                except TypeError:
                    continue

                if form1.is_valid():
                    print("valid")
                    obj = form1.save(commit=False)

                    obj.old_name = data4['NAME']
                    obj.old_url = data4['URL']
                    obj.old_desc = data4['DESC']
                    obj.old_brand = data4['BRAND']
                    obj.old_product_desc = data4['PRODUCT_DESC']
                    obj.asin = i

                    obj.save()

                    if sendme.extracted == False:
                        sendme.extracted=True
                        sendme.save()
                    return HttpResponseRedirect('/fetch_asin')
                else:
                    print(form1.errors)











    context = {
        'total_asin':total_asin,
        'fetch_asin':fetch_asin
    }

    return render(request,'fetch_asin.html',context=context)



def index(request):
    form5 = forms.form_empDetail()
    if(request.method=='POST'):
        form5 = forms.form_empDetail(request.POST)
        email = request.POST.get('email1')
        password = request.POST.get('pass1')

        conn = http.client.HTTPConnection("textmercato.com:4523")
        payload = "email="+email+"&password="+password
        headers = {
                'authorization': "Basic YWRtaW4tZGV2OmFkbWluUGFzcy0tMTIz",
                'content-type': "application/x-www-form-urlencoded",
                'cache-control': "no-cache",
                'postman-token': "5ac9f9ac-261e-c0ff-ee9b-65064632ba6e"
                }

        conn.request("POST", "/signin", payload, headers)

        res = conn.getresponse()
        data = res.read()

        data1 = data.decode("utf-8")
        data2 = ast.literal_eval(data1)
        status = data2["status"]
        first_name = data2["data"]["first_name"]
        last_name = data2["data"]["last_name"]
        name = first_name+" "+last_name
        request.session['name'] = name
        request.session['email'] = email

        roles = data2["data"]["roles"][0]
        email = data2["data"]["email"]

        try:
            if empDetail.objects.get(email=email):
                print("User already exists")

            else:
                if form5.is_valid():
                    obj5 = form5.save(commit=False)
                    obj5.name=name
                    obj5.email=email
                    obj5.roles=roles
                    obj5.save()
        except empDetail.DoesNotExist:
            #user is visiting first time
            if form5.is_valid():
                obj5 = form5.save(commit=False)
                obj5.name=name
                obj5.email=email
                obj5.roles=roles
                obj5.save()












        if status == "success":
            if roles == "admin":
                return HttpResponseRedirect('/manager')
            else:
                return HttpResponseRedirect('/detail')



        else:
            return HttpResponseRedirect('/')


    return render(request,'index.html')


def manager(request):
    data1 = asinDetail.objects.all()
    total_asin = data1.count()

    data2 = asinDetail.objects.filter(status=True)
    done_asin = data2.count()

    data3 = empDetail.objects.filter(~Q(roles="admin"))
    total_user = data3.count()

    data4 = asinDetail.objects.filter(extracted=True)
    asin_fetch = data4.count()







    context = {
        'total_asin':total_asin,
        'done_asin':done_asin,
        'total_user':total_user,
        'asin_fetch':asin_fetch,
        'data3':data3
        }
    return render(request,'manager.html',context=context)



def parse(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    r = requests.get(url,headers=headers)
    for i in range(20):
        try:

            soup = BeautifulSoup(r.content, 'html5lib')
            desc_list=[]

            doc = html.fromstring(r.content)
            XPATH_NAME = '//h1[@id="title"]//text()'
            XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
            XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
            XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
            XPATH_AVAILABILITY = '//div[@id="availability"]//text()'


            RAW_NAME = doc.xpath(XPATH_NAME)
            RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
            RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
            RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
            RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)


            NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
            SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
            CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
            ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
            AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None

            try:
                data1 = soup.find('div',{'class':'a-section a-spacing-medium a-spacing-top-small'})
                for data2 in data1.find_all('span',{'class':'a-list-item'}):
                    desc_list.append(data2.text)

                data2 = soup.find('td',{'class':'value'})
                brand = data2.text


                data3 = soup.find('div',{'id':'productDescription'})
                data4 = data3.find('p')
                productDescription = data4.text


                # data5 = soup.find('div',{'id':'dpx-aplus-product-description_feature_div'})
                # data6 = data5.find('div',{'id':'aplus_feature_div'})
                # data7 = data6.find('div',{'class':'a-section a-spacing-extra-large bucket'})
                # data8 = data7.find('div',{'class':'aplus-v2 desktop celwidget'})
                # for data10 in data8.find_all('h4'):
                #     h.append(data10.text)
                # for data11 in data8.find_all('p'):
                #     p.append(data11.text)







            except TypeError or ValueError:
                continue



            if not ORIGINAL_PRICE:
                ORIGINAL_PRICE = SALE_PRICE
            if not NAME :
                raise ValueError('Product not found!')

            # over = zip(h,p)

            data = {
                    'NAME':NAME,
                    'SALE_PRICE':SALE_PRICE,
                    'CATEGORY':CATEGORY,
                    'ORIGINAL_PRICE':ORIGINAL_PRICE,
                    'AVAILABILITY':AVAILABILITY,
                    'URL':url,
                    'DESC':desc_list,
                    'BRAND':brand,
                    'PRODUCT_DESC':productDescription,
                    # 'OVER':over
                    }

            return data
        except Exception as e:
            print(e)



#
# def detail(request):
#     name = request.session.get('name')
#     email = request.session.get('email')
#
#     if asinDetail.objects.filter(status=False).filter(email=email).filter(extracted=True).exists():
#         data2 = asinDetail.objects.filter(status=False, extracted=True, email=email)
#         for i in data2:
#             i = i.asin
#             print(i)
#             data3 = oldDetailAmazon.objects.get(asin=i)
#             form1 = forms.form_newProductDetail()
#             form2 = forms.form_oldProductDetail()
#             context = {
#                 'data3':data3,
#                 'form1':form1,
#                 'form2':form2,
#                 'name':name
#                 }
#
#             if request.method == 'POST':
#                 newtitle = request.POST.get('newtitle')
#                 form1 = forms.form_newProductDetail(request.POST)
#                 form2 = forms.form_oldProductDetail(request.POST)
#                 sendme = asinDetail.objects.get(asin=i)
#
#                 if form1.is_valid() and form2.is_valid():
#                     obj = form1.save(commit=False)
#                     obj.asin=i
#                     obj.save()
#
#                     obj1 = form2.save(commit=False)
#                     obj1.asin=i
#                     obj1.current_Title=data3.old_name
#                     obj1.revised_Title=form1.cleaned_data['title']
#                     obj1.save()
#
#                     data7 = empDetail.objects.get(email=email)
#                     data7.asin_done_c = F('asin_done_c') + 1
#                     data7.save()
#
#                     if sendme.status == False:
#                         sendme.status=True
#                         sendme.save()
#
#
#
#
#
#
#
#
#                 # with open('asinn.csv', 'r') as fin:
#                 #     data = fin.read().splitlines(True)
#                 # with open('asinn.csv', 'w') as fout:
#                 #     fout.writelines(data[1:])
#                 return HttpResponseRedirect('/detail')
#
#
#
#
#         return render(request,'detail.html',context=context)
#     else:
#         return HttpResponseRedirect('/message')
#

def detail(request):
    name = request.session.get('name')
    email = request.session.get('email')
    if asinDetail.objects.filter(email=email).filter(status=False).filter(extracted=True).exists():

        data1 = asinDetail.objects.filter(email=email).filter(status=False).filter(extracted=True)
        for i in data1:
            asin = i.asin

            if oldDetailAmazon.objects.filter(status=False).filter(asin=asin):
                #---->>>><<<<<-----#
                data2 = oldDetailAmazon.objects.get(asin=asin)
                #---->>>><<<<<-----#
                form1 = forms.form_newProductDetail()
                form2 = forms.form_oldProductDetail()

                data4 = ast.literal_eval(data2.old_desc)

                print(type(data2.old_desc))

                context = {
                    'data2':data2,
                    'name':name,
                    'data4':data4,
                    'form1':form1,
                    'form2':form2

                    }
                if request.method == 'POST':
                    newtitle = request.POST.get('newtitle')
                    form1 = forms.form_newProductDetail(request.POST)
                    form2 = forms.form_oldProductDetail(request.POST)
                    sendme = asinDetail.objects.get(asin=asin)
                    sendme1 = oldDetailAmazon.objects.get(asin=asin)



                    if form1.is_valid() and form2.is_valid():
                        obj = form1.save(commit=False)
                        obj.asin=asin
                        obj.save()

                        obj1 = form2.save(commit=False)
                        obj1.asin=i
                        obj1.current_Title=data2.old_name
                        obj1.revised_Title=form1.cleaned_data['title']
                        obj1.save()

                        data7 = empDetail.objects.get(email=email)
                        data7.asin_done_c = F('asin_done_c') + 1
                        data7.save()

                        if sendme.status == False:
                            sendme.status=True
                            sendme.save()

                        if sendme1.status == False:
                            sendme1.status=True
                            sendme1.save()
                        return HttpResponseRedirect('/detail')





                return render(request,'detail.html',context=context)
    else:
        return HttpResponseRedirect('/message')
