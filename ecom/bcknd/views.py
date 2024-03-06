from django.shortcuts import render, redirect
from . models import Datas, Category, Product
from django . core.files.storage import FileSystemStorage
from django.utils. datastructures import MultiValueDictKeyError
from frontnd. models import Contact
from django.contrib import messages

# Create your views here.   

def data(request):
    if request.method=='POST':
        name = request.POST['name']
        place = request.POST['place']
        mobile = request.POST['mobile']
        image = request.FILES['image'] 
        ecom = Datas(name=name, place=place, mobile=mobile, image=image)
        ecom.save()
    return render(request, 'data.html')

def display(request):
    dataa=Datas.objects.all()
    return render(request, 'display.html', {'dataa':dataa})

def catdata(request):
    if request.method=='POST':
        name = request.POST.get('category')
        description = request.POST['description']
        image = request.FILES['image']
        cate = Category(category=name, description=description, image=image)
        cate.save()
        messages.success(request, "Category saved Successfully")
        
    return render(request, 'catedata.html')

def catedisplay(request):
    cat=Category.objects.all()
    return render(request, 'catedisplay.html', {'cat':cat})

def catedelete(request, id):
    cate = Category.objects.get(id=id)
    cate.delete()
    return redirect(catedisplay)


def index(request):
    return render(request, 'index.html')


def prodata(request):
    if request.method=='POST':
        cname = request.POST.get('cname')
        pname = request.POST.get('pname')
        prize = request.POST.get('prize')
        size = request.POST.get('size')
        description = request.POST.get('description')
        image = request.FILES['image']
        cate = Product(cname=cname, pname=pname, prize=prize, size=size, description=description, image=image)
        cate.save()
        messages.success(request, "Prodjuct saved Successfully") 
    return render(request, 'prodata.html') 

def prodisplay(request):
    catt=Category.objects.all()
    pro=Product.objects.all()
    return render(request, 'prodisplay.html', {'pro':pro, 'catt':catt})

def proedit(request, id):
    proo=Product.objects.get(id=id)
    if request.method=="POST":
        cname = request.POST.get('cname') 
        pname = request.POST.get('pname') 
        size = request.POST.get('size') 
        prize = request.POST.get('prize') 
        description = request.POST.get('description') 
        img = request.POST.get('image')

        proo.cname=cname
        proo.pname=pname
        proo.size=size
        proo.prize=prize
        proo.description=description
        proo.image=img
        proo.save()
        return redirect('prodisplay')
    return render(request, 'proedit.html', {'proo':proo})

def prodelete(request, id):
    pro = Product.objects.get(id=id)
    pro.delete()
    return redirect(prodisplay)

def usrcontact(request):
    usr = Contact.objects.all()
    return render(request, 'usrcontact.html', {'usr':usr})

def usrcontactdelete(request, id):
    usr = Contact.objects.get(id=id)
    usr.delete()
    return redirect('usrcontact')
