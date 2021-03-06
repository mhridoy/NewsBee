from django.shortcuts import render,redirect,HttpResponseRedirect

from .forms import SignupForm, LoginForm, PostForm
from django.contrib import  messages
from django.contrib.auth import authenticate,login,logout
from .models import Post,Home,UserCountry,SaveCountry
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

        if 'name' in request.GET:
            name=request.GET['name']

            id = request.user.id 
           
            url = 'http://api.mediastack.com/v1/news?access_key=5b7237da6ecd7b298ec9aefc51acb02b&language=en&offset=0&limit=100&keywords='+name
            r = requests.get(url=url)
                #print(r.json())
            res=r.json()
            datas = res['data']
            collection=[]
            for i in datas:
                if i['image'] is None:
                    continue
                else:
                    collection.append(i)
            # for i in datas:
            #     news_data = Home(
            #     title= i['title'],
            #     category=i['category'],
            #     desc=i['description'],
            #     image_url=i['image'],
            #     url = i['url'],
            #     country=i['url'],


            #     )
            #news_data.save()
            #all_data= Home.objects.all()
            all_data=collection
                # else:
            # print("")
            # print("**********************************")
                #print(uc)
                # response =response['country']
                #for i in range(len(res['title'])):
                #    response.append(res['title'][i])

            return render (request,'blog/home.html',{'all_data':all_data})

        else:
            id = request.user.id
            Home.objects.all().delete()
            usercountry = UserCountry.objects.filter(user__id=id)
                # if len(usercountry) ==1:
                #print("No record!")
            uc = usercountry[0].country
            url = 'http://api.mediastack.com/v1/news?access_key=5b7237da6ecd7b298ec9aefc51acb02b&language=en&offset=0&limit=100&countries='+uc
            r = requests.get(url=url)
                #print(r.json())
            res=r.json()
            datas = res['data']
            collection=[]
            for i in datas:
                if i['image'] is None:
                    continue
                else:
                    #collection.append(i)
                    # collection= collection +i['category']
                    # collection= collection +i['description']
                    # collection= collection +i['image']
                    # collection= collection +i['published_at']
                    # collection= collection +i['country']
                    # collection= collection +i['url']
                    # collection= collection +i['description']
                    # collection= collection +i['image']
                    news_data = Home(
                    title= i['title'],
                    category=i['category'],
                    desc=i['description'],
                    image=i['image'],
                    url = i['url'],
                    country=i['country'],
                    published_at = i['published_at'],
                    )
                

                    news_data.save()
            all_data= Home.objects.all()
            #print("===================================")
            #print(collection)
            #all_data=collection
                # else:
            # print("")
            # print("**********************************")
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
        posts = Home.objects.all()
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
    posts = SaveCountry.objects.all()
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
            
            return redirect('/login/')
            # UserCountry.objects.get(user__id=3).country
    else:
        form = SignupForm()
        
    return render(request,'blog/signup.html',{'form':form,'posts':posts})

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
                messages.success(request,'Add News Successfully')
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
            pi = Home.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                messages.success(request,'Update News Successfully')
                form.save()
        else:
            pi = Home.objects.get(pk=id)
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

def generate_country_list(request):
    url = 'http://api.mediastack.com/v1/news?access_key=5b7237da6ecd7b298ec9aefc51acb02b&offset=0&limit=100'
    r = requests.get(url=url)
                #print(r.json())
    res=r.json()
    datas = res['data']
    for i in datas:
        news_data = SaveCountry(
        s_count= i['country']
                )
        news_data.save()
    all_contries = SaveCountry.objects.all()
    return None