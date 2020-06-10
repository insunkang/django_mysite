from django.shortcuts import render
from datetime import datetime
import random
# Create your views here.
def index(request):
    return render(request,'index.html')

def hello(request):
    menu = ['닭갈비','탕수육','초밥','스파게티돈까스']
    pick = random.choice(menu)
    return render(request,'hello.html', {'pick':pick})

def name(request):
    my_name = '강인선'
    return render(request,'name.html',{'my_name':my_name})
def introduce(request):
    my_info = ['강인선','게임','집돌이']
    name = '강인선'
    age = '40'
    me = '집돌이'
    context = {
        'name2' : name,
        'age' : age,
        'me' : me,
        'ios' : 'ios',
        'location':'멀캠'
    }
    return render(request, 'introduce.html',context)
def newpage(request):
    ids = ['부러럭','DQxxx','한숨잘란다','peiry','우황좌황청심환','강인선인장']
    pickids = random.choice(ids)
    return render(request,'newpage.html',{'id':pickids})

def yourname(request,name,age):
    #name =name
    context={
        'name' : name,
        'age' : age
    }
    return render(request,'yourname.html',context)
def multi(request,num1,num2):
    context={
        'num1' : num1,
        'num2' : num2,
        'num3' : num1*num2
    }
    return render(request,'multi.html',context)
def multitab(request,num1,num2):
    answer = []
    if num1<num2:
        num2,num1=num1,num2
    for data in range(1,num1+1):
        answer.append(num2*data)

    return render(request,'multitab.html',{'answer':answer})

def dtl(request):
    my_list = ['짜장면','차돌짬뽕','탕수육']
    empty_list = []
    my_string = "Life is short, you need Python"
    today = datetime.now()
    context = {
        'my_list' : my_list,
        'empty_list' : empty_list,
        'my_string' : my_string,
        'today' : today
    }
    return render(request, 'dtl.html',context)

def forif(request,strinput):
    my_list = [100, 50, 30, 20, 10]
    my_string = '간단한 문자열'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'my_list' : my_list,
        'my_string' : my_string,
        'data_a' : data_a,
        'data_b' : data_b,
        'input' : strinput
    
    }
    return render(request, 'forif.html', context)
