
from django.shortcuts import render, redirect
from bcknd.models import Category, Product
from frontnd . models import Contact, Register, cart

# Create your views here. 

def home(request):
    pro = Product.objects.all() 
    cate = Category.objects.all() 
    return render (request, 'home.html',{'pro':pro, 'cate':cate})

def myaccount(request):
    return render(request, 'myaccount.html')

def category(request):
    pro = Product.objects.all()
    cate = Category.objects.all()
    return render(request, 'category.html', {'pro':pro, 'cate':cate})

def product(request, catname):
    pro = Product.objects.filter(cname=catname) 
    cate = Category.objects.all()
    return render(request, 'product.html', {'pro':pro, 'cate':cate})

def singleproduct(request, id):
    cate = Category.objects.all()
    pro = Product.objects.get(id=id)
    return render(request, 'singleproduct.html',{'pro':pro, 'cate':cate})

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        usr = Contact(name=name, email=email, subject=subject, message=message)
        usr.save()
    return render(request, 'contact.html')

def userlogn(request):
    if request.method=='POST':
        name = request.POST['name']
        password = request.POST['password']
        if Register.objects.filter(name=name, password=password).exists():
            request.session['name']=name
            request.session['password']=password
            return redirect(home)
        else:
            return redirect(userlogn)

    return render(request, 'userlogn.html')

def userlogout(request):
    del request.session['name']
    del request.session['password']
    return redirect(userlogn)

def cart(request):
    if request.method=='POST':
        image = request.FILES['image']
        username = request.POST['username']
        productname = request.POST['productname']
        quantity = request.POST['quantity']
        price = request.POST['price']
        totalprice = request.POST['totalprice']
        cartt=cart(image=image, username=username, productname=productname, quantity=quantity, price=price, totalprice=totalprice)
        cartt.save()
    return render(request, 'cart.html')

def cartdisplay(request):
    cate = Category.objects.all()
    cartt=cart.objects.filter(username=request.session['name'])
    return render(request, 'cart.html', {'cartt':cartt, 'cate':cate})

def cartdelete(request, id):
    cartt=cart.objects.get(id=id)
    cartt.delete()
    return redirect(cartdisplay)  

def whish(request):
    return render(request, 'whish list.html')