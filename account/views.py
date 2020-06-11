from django.shortcuts import render,redirect
from django.contrib.auth.models import User #유저에 대한 클래스
from django.contrib import auth #계정에 대한 권한

# Create your views here.
def signup(request): #회원가입
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
            auth.login(request,user) #회원가입후 자동으로 로그인
            return redirect('home')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        #데이터베이스에 회이 맞는지
        if user is not None: # 회원이라면
            auth.login(request,user) #로그인
            return redirect('home')#home으로 이동
        else: #회원이 아니라면  에러출력
            return render(request,'login.html',{'error' : '회원이 아닙니다.'})
    else:
        return render(request,'login.html')

def logout(request): #로그아웃
    auth.logout(request)
    return render(request,'home.html') 

def create(request):
    user = User()
    user.username = request.GET['username']
    user.password = request.GET['password']
    user.email = request.GET['email']
    user.save()
    return redirect('home.html')









    