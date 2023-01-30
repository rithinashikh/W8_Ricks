from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import UserDetails, Products, Category
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def userlogin(request):
    if 'username' in request.session:
        return redirect('shop')
    else:
        if request.method=='POST':
            username=request.POST.get('c_username')
            pass1=request.POST.get('c_password')
            user=UserDetails.objects.filter(username=username,password=pass1).count()
            valid_user = UserDetails.objects.filter(username=username).all()
            for filter_user in valid_user:
                user=UserDetails.objects.filter(username=username,password=pass1).count()
                if filter_user.active:
                    if user==1:
                        request.session['username']=username
                        return redirect('shop')
                    else:
                        messages.warning(request, 'Username or Password incorrect!!')
                        return render (request, 'userlogin.html')
                else:
                    messages.warning(request, 'User is blocked by Admin')
                    return render (request, 'userlogin.html')                    
        return render (request, 'userlogin.html')

def usersignup(request):
    if request.method=='POST':
        username=request.POST.get('c_username')
        email=request.POST.get('c_email')
        password=request.POST.get('c_password1')
        password2=request.POST.get('c_password2')
        if password==password2:
            if UserDetails.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('usersignup')
            elif UserDetails.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('usersignup')
            else:
                foo_instance = UserDetails.objects.create(username=username,email=email,password=password)
                foo_instance.save()
                return redirect('userlogin')
                
        else:
            messages.info(request, 'password not matching')
            return redirect('usersignup')       
        
    else:    
        return render (request, 'usersignup.html')

def shop(request):
    if 'username' in request.session:
        details3=Products.objects.all()
        return render(request, 'shop.html', {'mymembers3': details3})
    else:
        return render(request, 'userlogin.html')



def userlogout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('userlogin')

def adminlogin(request):
    if 'username' in request.session:
        return redirect('admindashboard')
    else:    
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password):
                request.session['username']=username
                return redirect('admindashboard')
                
            else:
                messages.warning(request, 'Username or Password incorrect!!')
                return render (request, 'adminlogin.html')

        return render(request, 'adminlogin.html')

def adminuserlist(request):
    if 'username' in request.session:
        if 'search' in request.GET:
            search=request.GET['search']
            details=UserDetails.objects.filter(username__icontains=search)
        else:
            details=UserDetails.objects.all()
        return render(request,'adminuserlist.html',{'mymembers': details})
    else:
        return render(request, 'adminlogin.html')

def userdelete(request):
    uid=request.GET['uid']
    UserDetails.objects.filter(id=uid).delete()
    return redirect('adminuserlist')

def admindashboard(request):
    if 'username' in request.session:
        return render(request, 'admindashboard.html')
    else:
        return render(request, 'adminlogin.html')

def userblock(request):
    uid=request.GET['uid']
    block_check=UserDetails.objects.filter(id=uid)
    for x in block_check:
        if x.active:
            UserDetails.objects.filter(id=uid).update(active=False)
        else:
            UserDetails.objects.filter(id=uid).update(active=True)

    return redirect('adminuserlist')

def adminlogout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('adminlogin')

def adminproductlist(request):
    if 'username' in request.session:
        if 'search' in request.GET:
            search=request.GET['search']
            details=Products.objects.filter(name__icontains=search)
        else:
            details2=Products.objects.all()
        return render(request,'adminproductlist.html',{'mymembers2': details2})
    else:
        return render(request, 'adminlogin.html')
    
def adminaddproduct(request):
    if 'username' in request.session:       
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            category_name = request.POST.get('category')
            category = Category.objects.filter(name=category_name).first()
            Products.objects.create(name=name,price=price,description=description,image=image, category=category)
            return redirect('adminproductlist')
        return render(request, 'adminaddproduct.html')
    else:
        return render(request, 'adminlogin.html')
    
def deleteproduct(request):
    uid=request.GET['uid']
    Products.objects.filter(id=uid).delete()
    return redirect('adminproductlist')

def updateproduct(request):  
    id=request.POST['uid']
    name = request.POST['name']
    price = request.POST['price']
    description = request.POST['description']
    image = request.FILES['image']
    category_name = request.POST['category']   
    category = Category.objects.filter(name=category_name).first()
    Products.objects.filter(id=id).update(name=name,price=price,description=description,image=image, category=category)
    print("Update successfull")
    return redirect('adminuserlist')

def shopsingle(request):
    if 'username' in request.session:
        uid=request.GET['uid']
        details4=Products.objects.filter(id=uid).first()
        print("details",details4)
        return render(request, 'shopsingle.html', {'mymembers4': details4})
    else:
        return render(request, 'userlogin.html')