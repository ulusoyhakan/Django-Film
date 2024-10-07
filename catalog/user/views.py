from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rePassword = request.POST['repassword']        

        if password == rePassword:
            if User.objects.filter(username=username).exists():
                messages.add_message(request,messages.WARNING, 'Bu kullanıcı adı daha önce alınmış')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request,messages.WARNING, 'Bu mail adı daha önce alınmış')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    messages.add_message(request,messages.SUCCESS, 'Kullanıcı oluşturuldu')
                    return redirect('login')
        else:
            print('parola eşleşmiyor')
            return redirect('register')
    else:
        return render(request, 'user/register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['loginName']
        password = request.POST['loginPassword']

        userAuth = auth.authenticate(username=username, password=password)
        if userAuth is not None:
            auth.login(request, userAuth)
            messages.add_message(request,messages.SUCCESS, 'Giriş Başarılı Hoşgeldiniz')
            return redirect('index')
        else:
            messages.add_message(request,messages.ERROR, 'Kullanıcı adı veya parola hatalı')
            print('var bir bokluk')
            return redirect('login')
    else:
        return render(request, 'user/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,'Çıkış Yapıldı')
        return redirect('index')

    else:
        return render(request, 'user/logout.html')