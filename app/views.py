from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from lxml import html
import csv,os,json
import requests
import pandas as pd
from . import forms
from .models import *
from bs4 import BeautifulSoup


def index(request):
    return render(request,'index.html')



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

            data1 = soup.find('div',{'class':'a-section a-spacing-medium a-spacing-top-small'})
            for data2 in data1.find_all('span',{'class':'a-list-item'}):
                desc_list.append(data2.text)

            if not ORIGINAL_PRICE:
                ORIGINAL_PRICE = SALE_PRICE
            if not NAME :
                raise ValueError('Product not found!')

            data = {
                    'NAME':NAME,
                    'SALE_PRICE':SALE_PRICE,
                    'CATEGORY':CATEGORY,
                    'ORIGINAL_PRICE':ORIGINAL_PRICE,
                    'AVAILABILITY':AVAILABILITY,
                    'URL':url,
                    'DESC':desc_list
                    }

            return data
        except Exception as e:
            print(e)



def detail(request):
    asin = pd.read_csv('asin.csv')
    for i in asin:
        form1 = forms.form_newProductDetail()
        form2 = forms.form_oldProductDetail()
        url = "http://www.amazon.in/dp/"+i
        data1 = parse(url)
        data1['asin']=i
        data1['form1']=form1
        data1['form2']=form2




        if request.method == 'POST':
            newtitle = request.POST.get('newtitle')
            form1 = forms.form_newProductDetail(request.POST)
            form2 = forms.form_oldProductDetail(request.POST)
            if form1.is_valid() and form2.is_valid():
                obj = form1.save(commit=False)
                obj.asin=i
                obj.save()

                obj1 = form2.save(commit=False)
                obj1.asin=i
                obj1.current_Title=data1['NAME']
                obj1.revised_Title=form1.cleaned_data['title']
                obj1.save()




            with open('asin.csv', 'r') as fin:
                data = fin.read().splitlines(True)
            with open('asin.csv', 'w') as fout:
                fout.writelines(data[1:])
            return HttpResponseRedirect('/detail')

        return render(request,'detail.html',context=data1)
