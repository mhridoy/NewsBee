from django.shortcuts import render,redirect,HttpResponseRedirect

from .forms import SignupForm, LoginForm, PostForm
from django.contrib import  messages
from django.contrib.auth import authenticate,login,logout
from .models import Post,Home,UserCountry
from django.contrib.auth.models import Group
import requests
# Home
def home(request):
    if request.user.is_authenticated:
        # url = 'http://api.mediastack.com/v1/news?access_key=5b7237da6ecd7b298ec9aefc51acb02b&language=en'

        # r = requests.get(url=url)
        # # print(r.json())
        # res=r.json()
        # data = res
        id = request.user.id
        usercountry = UserCountry.objects.filter(user__id=3)
        # if len(usercountry) ==1:
        print("No record!")
        uc = usercountry[0].country
        url = 'http://api.mediastack.com/v1/news?access_key=5b7237da6ecd7b298ec9aefc51acb02b&language=en&countries='+uc
        r = requests.get(url=url)
        print(r.json())
        res=r.json()
        datas = res['data']

        for i in datas:
            news_data = Home(
                title= i['title'],
                category=i['category'],
                desc=i['description'],
                image_url=i['image'],

            )
            news_data.save()
            all_data= Home.objects.all()
        # else:
        print("")
        print("**********************************")
        #print(uc)
        # response =response['country']
        #for i in range(len(res['title'])):
        #    response.append(res['title'][i])

        return render (request,'blog/home.html',{'all_data':all_data})
    else:
        return redirect('/login/')
def about(request):
    return render(request,'blog/about.html')


#Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name= user.get_full_name()
        gps = user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return redirect('/login/')

#Logout
def user_logout(request):
    logout(request)
    return redirect('/')
#Signup
def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        country = request.POST['country']
        print("====================================================")
        # print(country)
        if form.is_valid():
            messages.success(request,'Congrats! You have become an Author')
            user = form.save()
            user_country = UserCountry()
            user_country.country = country
            user_country.user = user
            user_country.save()
            # UserCountry.objects.get(user__id=3).country
    else:
        form = SignupForm()
    return render(request,'blog/signup.html',{'form':form})

#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully!')
                    return redirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return redirect('/dashboard/')

#Add New Post

def add_post(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title,desc=desc)
                messages.success(request,'Add Post Successfully')
                pst.save()
                form = PostForm()

        else:
            form = PostForm()

        return render(request,'blog/addpost.html',{'form':form})
    else:
        return redirect('/login/')

#Update Post

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                messages.success(request,'Update Post Successfully')
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)        
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return redirect('/login/')

8
#Delete Post

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return redirect('/dashboard/')
    else:
        return redirect('/login/')